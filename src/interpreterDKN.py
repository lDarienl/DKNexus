#!/usr/bin/env python3
"""
Intérprete del DSL DKNexus usando ANTLR4 y patrón Visitor.
Ejecutar desde el directorio del proyecto (donde están los .py generados por ANTLR).
"""

import dataDKN
import mathDKN
import matrixDKN
import persistDKN
from heapDKN import DKNMemoryError, HeapManager
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from grammarDKNLexer import grammarDKNLexer
from grammarDKNParser import grammarDKNParser
from grammarDKNVisitor import grammarDKNVisitor


class DKNRuntimeError(Exception):
    pass


class DKNParseError(Exception):
    pass


class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Mensajes un poco más amigables para errores comunes
        friendly = msg
        if "missing ';'" in msg:
            friendly = "Falta ';' al final de la instrucción."
        elif "token recognition error at" in msg:
            friendly = msg.replace("token recognition error at:", "Token inválido:")
        elif "mismatched input ',' expecting ')'" in msg:
            friendly = "Llamada a función mal formada: cantidad de argumentos incorrecta."
        elif "no viable alternative" in msg:
            friendly = "Error de sintaxis: expresión/instrucción mal formada."
        self.errors.append(f"L{line}:{column} {friendly}")


class EvalVisitor(grammarDKNVisitor):
    """Visitor que evalúa expresiones y ejecuta sentencias."""

    def __init__(self, heap_slots: int | None = None, instruction_limit: int = 1_000_000):
        # heap_slots=None => heap dinamico (sin limite rigido de 1024), apto para
        # vectores/matrices grandes de Machine Learning.
        self.heap = HeapManager(heap_slots)
        # Cada ámbito mapea nombre -> dirección (puntero) en el heap.
        self.scopes: list[dict[str, str]] = [{}]
        self.functions = {}
        self._returned = False
        self.return_value = None
        self._instr_count = 0
        self._instr_limit = instruction_limit

    def _bump_instruction(self, cost: int = 1) -> None:
        """Execution guard: evita bucles infinitos / ejecución excesiva."""
        self._instr_count += cost
        if self._instr_count > self._instr_limit:
            raise DKNRuntimeError(
                "Timeout/Infinite Loop detected (límite de operaciones de ejecución excedido)."
            )

    def _push_scope(self):
        self.scopes.append({})

    def _pop_scope(self):
        if len(self.scopes) <= 1:
            raise DKNRuntimeError("Error interno: no se puede cerrar el ámbito global.")
        dead = self.scopes.pop()
        for _name, addr in dead.items():
            self.heap.free(addr)

    def _lookup_var(self, name):
        for d in reversed(self.scopes):
            if name in d:
                addr = d[name]
                try:
                    return self.heap.read(addr)
                except KeyError:
                    raise DKNRuntimeError(
                        f"Error Semántico: puntero inválido o memoria liberada para '{name}'."
                    ) from None
        raise DKNRuntimeError(f"Error Semántico: La variable '{name}' no ha sido declarada.")

    def _lookup_ptr(self, name):
        for d in reversed(self.scopes):
            if name in d:
                return d[name]
        return None

    def _lookup_var_optional(self, name):
        for d in reversed(self.scopes):
            if name in d:
                addr = d[name]
                try:
                    return self.heap.read(addr)
                except KeyError:
                    raise DKNRuntimeError(
                        f"Error Semántico: puntero inválido o memoria liberada para '{name}'."
                    ) from None
        return None

    def _assign_var(self, name, value):
        new_addr = self.heap.allocate(value)
        found_scope = None
        for d in reversed(self.scopes):
            if name in d:
                found_scope = d
                break
        if found_scope is not None:
            old_addr = found_scope[name]
            found_scope[name] = new_addr
            self.heap.free(old_addr)
            return self.heap.read(new_addr)
        self.scopes[-1][name] = new_addr
        return self.heap.read(new_addr)

    def _require_str(self, value, what="texto"):
        if not isinstance(value, str):
            raise DKNRuntimeError(f"Tipo de dato inválido: Se esperaba un string ({what}).")
        return value

    def _to_bool(self, value):
        """Truthiness estilo Python: 0/vacío/None -> False; resto -> True."""
        return bool(value)

    def _type_name(self, value):
        if value is None:
            return "none"
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "str"
        if isinstance(value, dict):
            return "dict"
        if matrixDKN.is_matrix(value):
            return "matrix"
        if isinstance(value, list):
            return "list"
        return type(value).__name__

    def _matches_type(self, value, type_name: str):
        t = type_name.lower()
        if t in ("number", "numeric"):
            return isinstance(value, (int, float))
        if t in ("int", "integer"):
            return isinstance(value, int) and not isinstance(value, bool)
        if t in ("float",):
            return isinstance(value, float)
        if t in ("bool", "boolean"):
            return isinstance(value, bool)
        if t in ("str", "string", "text"):
            return isinstance(value, str)
        if t in ("list",):
            return isinstance(value, list) and not matrixDKN.is_matrix(value)
        if t in ("matrix",):
            return matrixDKN.is_matrix(value)
        if t in ("none", "null"):
            return value is None
        return False

    def _expr0(self, ctx):
        """
        En contextos genéricos ANTLR genera expr(i). En contextos etiquetados
        (p.ej. AsignacionContext) genera expr() sin índice.
        """
        try:
            return ctx.expr(0)
        except TypeError:
            return ctx.expr()

    def _require_number(self, value):
        if not isinstance(value, (int, float)):
            raise DKNRuntimeError("Tipo de dato inválido: Se esperaba un número.")
        return value

    def _coerce_int_index(self, value, builtin_name: str):
        """Índice entero para columnas (rechaza bool y floats no enteros)."""
        if isinstance(value, bool):
            raise DKNRuntimeError(
                f"{builtin_name}: el índice de columna no puede ser un booleano."
            )
        if not isinstance(value, (int, float)):
            raise DKNRuntimeError(
                f"{builtin_name}: el índice de columna debe ser un número entero."
            )
        fv = float(value)
        if fv != int(fv):
            raise DKNRuntimeError(
                f"{builtin_name}: el índice de columna debe ser un entero (se recibió {value!r})."
            )
        return int(fv)

    def _reject_nan(self, value):
        # NaN es el único valor que no es igual a sí mismo en Python
        if isinstance(value, float) and value != value:
            raise DKNRuntimeError("Operación inválida: El resultado es un valor indeterminado (NaN).")
        return value

    def _is_matrix(self, v):
        return matrixDKN.is_matrix(v)

    def visitProgram(self, ctx):
        for item in ctx.programItem():
            if self._returned:
                break
            self.visit(item)
        return None

    def visitItemFunc(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        self.visit(ctx.functionDef())
        return None

    def visitItemStmt(self, ctx):
        if self._returned:
            return None
        self.visit(ctx.statement())
        return None

    def visitFunctionDefRule(self, ctx):
        toks = ctx.VARIABLE()
        if toks is None:
            raise DKNRuntimeError("Definición de función inválida: falta el nombre.")
        if not isinstance(toks, list):
            toks = [toks]
        names = [t.getText() for t in toks]
        fname = names[0]
        params = names[1:]
        self.functions[fname] = {"params": params, "statements": list(ctx.statement())}
        return None

    def visitStatement(self, ctx):
        # Con alternativas etiquetadas (#PrintExpr, #IfStmt, etc.) ANTLR llamará
        # a los métodos específicos. Este método queda como fallback.
        return self.visitChildren(ctx)

    # ---- Statement visitors (etiquetas actuales en grammarDKN.g4) ----
    def visitPrintExpr(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        self.visit(self._expr0(ctx))
        return None

    def visitAsignacion(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        name = ctx.VARIABLE().getText()
        value = self.visit(self._expr0(ctx))
        return self._assign_var(name, value)

    def visitIndexAssign(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        name = ctx.VARIABLE().getText()
        container = self._lookup_var(name)
        key_raw = self.visit(ctx.expr(0))
        if isinstance(container, dict):
            key = self._dict_key(key_raw)
            value = self.visit(ctx.expr(1))
            container[key] = value
            return value
        if not isinstance(container, list):
            raise DKNRuntimeError(f"Error Semántico: '{name}' no es indexable como lista o diccionario.")
        idx = self._coerce_int_index(key_raw, "index")
        if idx < 0 or idx >= len(container):
            raise DKNRuntimeError(
                f"Error de índice: posición {idx} fuera de rango para '{name}' (longitud {len(container)})."
            )
        value = self.visit(ctx.expr(1))
        container[idx] = value
        return value

    def visitAssignExpr(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        return self._assign_var(name, value)

    def visitNotExpr(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        return not self._to_bool(self.visit(ctx.expr()))

    def visitAndExpr(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        left = self.visit(ctx.expr(0))
        # Cortocircuito: si left es falsy, no evaluar right.
        if not self._to_bool(left):
            return False
        return self._to_bool(self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        left = self.visit(ctx.expr(0))
        # Cortocircuito: si left es truthy, no evaluar right.
        if self._to_bool(left):
            return True
        return self._to_bool(self.visit(ctx.expr(1)))

    def visitIfStmt(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        cond = self.visit(self._expr0(ctx))
        if cond:
            for st in ctx.statement():
                if self._returned:
                    break
                self._bump_instruction()
                self.visit(st)
        return None

    def visitWhileStmt(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        # expr ')' '{' statement+ '}'
        while True:
            self._bump_instruction()
            if not self.visit(self._expr0(ctx)):
                break
            self._bump_instruction()
            for st in ctx.statement():
                if self._returned:
                    break
                self._bump_instruction()
                self.visit(st)
            if self._returned:
                break
        return None

    def visitForStmt(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        # for '(' expr ';' expr ';' expr ')' '{' statement+ '}'
        self.visit(ctx.expr(0))  # init
        while True:
            self._bump_instruction()
            if not self.visit(ctx.expr(1)):
                break
            self._bump_instruction()
            for st in ctx.statement():
                if self._returned:
                    break
                self._bump_instruction()
                self.visit(st)
            if self._returned:
                break
            self.visit(ctx.expr(2))  # update
        return None

    def visitStackPushStmt(self, ctx):
        self._bump_instruction()
        name = ctx.VARIABLE().getText()
        val = self.visit(ctx.expr())
        cur = self._lookup_var_optional(name)
        if cur is None:
            self._assign_var(name, [])
            cur = self._lookup_var(name)
        if not isinstance(cur, list):
            raise DKNRuntimeError(f"Error Semántico: '{name}' no es una lista/pila.")
        cur.append(val)
        return None

    def visitQueueEnqueueStmt(self, ctx):
        self._bump_instruction()
        name = ctx.VARIABLE().getText()
        val = self.visit(ctx.expr())
        cur = self._lookup_var_optional(name)
        if cur is None:
            self._assign_var(name, [])
            cur = self._lookup_var(name)
        if not isinstance(cur, list):
            raise DKNRuntimeError(f"Error Semántico: '{name}' no es una lista/cola.")
        cur.append(val)
        return None

    def visitExpr(self, ctx):
        # Nota: Con alternativas etiquetadas en ANTLR (p.ej. #SumaResta),
        # normalmente se llaman métodos visitSumaResta/visitMulDivMod/etc.
        # Este método se mantiene como fallback para contextos no etiquetados.
        # NUMBER
        if ctx.NUMBER():
            s = ctx.NUMBER().getText()
            return float(s) if '.' in s else int(s)
        # VARIABLE
        if ctx.VARIABLE():
            name = ctx.VARIABLE().getText()
            return self._lookup_var(name)
        # expr op expr (binario)
        if ctx.expr() and len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            if op == '-':
                return left - right
            if op == '*':
                return left * right
            if op == '/':
                return left / right if right != 0 else 0
            if op == '%':
                return left % right if right != 0 else 0
            if op == '^':
                return left ** right
        # ( expr ) o sin/cos/tan( expr )
        if ctx.expr() and len(ctx.expr()) == 1:
            first = ctx.getChild(0).getText()
            val = self.visit(ctx.expr(0))
            if first == '(':
                return val
            if first == 'sin':
                return mathDKN.sin(val)
            if first == 'cos':
                return mathDKN.cos(val)
            if first == 'tan':
                return mathDKN.tan(val)
        return None

    # ---- Expr visitors (etiquetas actuales en grammarDKN.g4) ----
    def visitNum(self, ctx):
        s = ctx.NUMBER().getText()
        return float(s) if '.' in s else int(s)

    def visitVar(self, ctx):
        name = ctx.VARIABLE().getText()
        return self._lookup_var(name)

    def visitStringLiteral(self, ctx):
        raw = ctx.STRING().getText()
        # Quitar comillas de los extremos y desescapar \"
        inner = raw[1:-1].replace('\\"', '"')
        return inner

    def visitIndexAccess(self, ctx):
        name = ctx.VARIABLE().getText()
        container = self._lookup_var(name)
        key_raw = self.visit(ctx.expr())
        if isinstance(container, dict):
            key = self._dict_key(key_raw)
            if key not in container:
                raise DKNRuntimeError(
                    f"Error de clave: '{key}' no existe en el diccionario '{name}'."
                )
            return container[key]
        if not isinstance(container, list):
            raise DKNRuntimeError(f"Error Semántico: '{name}' no es indexable como lista o diccionario.")
        idx = self._coerce_int_index(key_raw, "index")
        if idx < 0 or idx >= len(container):
            raise DKNRuntimeError(
                f"Error de índice: posición {idx} fuera de rango para '{name}' (longitud {len(container)})."
            )
        return container[idx]

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    # ---- Infraestructura ML (Paso 1): métricas y canvas ASCII (sin librerías) ----

    def _ml_vector(self, value, fname, argname):
        """Extrae un vector numérico (lista de floats) desde un valor del Heap."""
        if not isinstance(value, list) or matrixDKN.is_matrix(value):
            raise DKNRuntimeError(
                f"{fname}: '{argname}' debe ser una lista/vector de números (1D)."
            )
        if not value:
            raise DKNRuntimeError(f"{fname}: '{argname}' no puede estar vacío.")
        out = []
        for v in value:
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise DKNRuntimeError(
                    f"{fname}: '{argname}' debe contener solo valores numéricos."
                )
            out.append(float(v))
        return out

    def _ml_binary(self, value, fname, argname):
        """Igual que _ml_vector pero exige etiquetas binarias (0 y 1)."""
        vec = self._ml_vector(value, fname, argname)
        out = []
        for v in vec:
            if v not in (0.0, 1.0):
                raise DKNRuntimeError(
                    f"{fname}: '{argname}' debe contener solo 0 y 1 (clasificación binaria)."
                )
            out.append(int(v))
        return out

    def _ascii_canvas(self, X, Y, weights=None, title="[Grafico]"):
        """
        Construye un canvas ASCII (~40x15) con la dispersión de (X, Y).
        Si `weights` no es None, dibuja además la recta y = W[0] + W[1]*x.
        Devuelve el string completo del canvas (con título).
        """
        WIDTH = 40
        HEIGHT = 15
        n = len(X)

        xmin, xmax = min(X), max(X)
        ymin, ymax = min(Y), max(Y)

        # Si hay recta, ampliamos el rango Y para que sea visible dentro del grid.
        if weights is not None:
            y_lo = weights[0] + weights[1] * xmin
            y_hi = weights[0] + weights[1] * xmax
            ymin = min(ymin, y_lo, y_hi)
            ymax = max(ymax, y_lo, y_hi)

        # Grid de caracteres inicializado en blanco.
        grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
        # Eje Y (columna 0) y eje X (última fila), con origen '+'.
        for r in range(HEIGHT):
            grid[r][0] = '|'
        for c in range(WIDTH):
            grid[HEIGHT - 1][c] = '-'
        grid[HEIGHT - 1][0] = '+'

        data_cols = WIDTH - 1   # columnas útiles 1..WIDTH-1
        data_rows = HEIGHT - 1  # filas útiles 0..HEIGHT-2

        def col_of(x):
            if xmax == xmin:
                scaled = 0
            else:
                scaled = int((x - xmin) / (xmax - xmin) * (data_cols - 1))
            return 1 + scaled

        def row_of(y):
            if ymax == ymin:
                scaled = 0
            else:
                scaled = int((y - ymin) / (ymax - ymin) * (data_rows - 1))
            # Invertir: los valores altos de Y van arriba.
            return (data_rows - 1) - scaled

        # Puntos de datos ('*'): un bump por cada punto procesado.
        for i in range(n):
            self._bump_instruction()
            c = col_of(X[i])
            r = row_of(Y[i])
            if 0 <= r < data_rows and 1 <= c < WIDTH:
                grid[r][c] = '*'

        # Recta de regresión / frontera de decisión ('#') sobre el canvas.
        if weights is not None:
            for c in range(1, WIDTH):
                if data_cols - 1 <= 0:
                    x = xmin
                else:
                    x = xmin + (c - 1) / (data_cols - 1) * (xmax - xmin)
                y = weights[0] + weights[1] * x
                r = row_of(y)
                if 0 <= r < data_rows and grid[r][c] == ' ':
                    grid[r][c] = '#'

        # Render por filas: un bump por cada fila renderizada del canvas.
        lines = [title]
        for r in range(HEIGHT):
            self._bump_instruction()
            lines.append(''.join(grid[r]))
        return '\n'.join(lines)

    def visitFuncCall(self, ctx):
        self._bump_instruction()
        name = ctx.VARIABLE().getText()
        arg_exprs = ctx.expr()

        if name == "isinstance":
            if not arg_exprs or len(arg_exprs) != 2:
                raise DKNRuntimeError("isinstance(x, tipo) requiere exactamente dos argumentos.")
            val = self.visit(arg_exprs[0])
            raw_type = arg_exprs[1].getText().strip()
            if raw_type.startswith('"') and raw_type.endswith('"'):
                raw_type = raw_type[1:-1].replace('\\"', '"')
            return self._matches_type(val, raw_type)

        args = [self.visit(e) for e in arg_exprs] if arg_exprs else []

        if name == "len":
            if len(args) != 1:
                raise DKNRuntimeError("len(x) requiere exactamente un argumento.")
            if not isinstance(args[0], (list, dict)):
                raise DKNRuntimeError("len(x) solo admite listas/matrices/diccionarios.")
            return len(args[0])

        if name == "dict":
            if len(args) != 0:
                raise DKNRuntimeError("dict() no recibe argumentos (crea un diccionario vacío).")
            return {}

        if name in ("keys", "values"):
            if len(args) != 1 or not isinstance(args[0], dict):
                raise DKNRuntimeError(f"{name}(d) requiere un diccionario.")
            seq = list(args[0].keys()) if name == "keys" else list(args[0].values())
            for _ in seq:
                self._bump_instruction()
            return seq

        if name == "has":
            if len(args) != 2 or not isinstance(args[0], dict):
                raise DKNRuntimeError("has(d, clave) requiere un diccionario y una clave.")
            return self._dict_key(args[1]) in args[0]

        if name == "del":
            if len(args) != 2 or not isinstance(args[0], dict):
                raise DKNRuntimeError("del(d, clave) requiere un diccionario y una clave.")
            key = self._dict_key(args[1])
            if key not in args[0]:
                raise DKNRuntimeError(f"del: la clave '{key}' no existe en el diccionario.")
            return args[0].pop(key)

        if name == "redis_set":
            if len(args) != 2:
                raise DKNRuntimeError("redis_set(clave, valor) requiere dos argumentos.")
            clave = self._require_str(args[0], "clave")
            try:
                persistDKN.store_set(clave, args[1])
            except Exception as e:
                raise DKNRuntimeError(f"redis_set: error de persistencia: {e}") from e
            return None

        if name == "redis_get":
            if len(args) != 1:
                raise DKNRuntimeError("redis_get(clave) requiere un argumento.")
            clave = self._require_str(args[0], "clave")
            try:
                return persistDKN.store_get(clave)
            except Exception as e:
                raise DKNRuntimeError(f"redis_get: error de persistencia: {e}") from e

        if name == "redis_del":
            if len(args) != 1:
                raise DKNRuntimeError("redis_del(clave) requiere un argumento.")
            clave = self._require_str(args[0], "clave")
            try:
                return persistDKN.store_del(clave)
            except Exception as e:
                raise DKNRuntimeError(f"redis_del: error de persistencia: {e}") from e

        if name == "redis_exists":
            if len(args) != 1:
                raise DKNRuntimeError("redis_exists(clave) requiere un argumento.")
            clave = self._require_str(args[0], "clave")
            try:
                return persistDKN.store_exists(clave)
            except Exception as e:
                raise DKNRuntimeError(f"redis_exists: error de persistencia: {e}") from e

        if name == "redis_keys":
            if len(args) != 0:
                raise DKNRuntimeError("redis_keys() no recibe argumentos.")
            try:
                return persistDKN.store_keys()
            except Exception as e:
                raise DKNRuntimeError(f"redis_keys: error de persistencia: {e}") from e

        if name == "store_backend":
            if len(args) != 0:
                raise DKNRuntimeError("store_backend() no recibe argumentos.")
            return persistDKN.backend_name()

        if name == "type":
            if len(args) != 1:
                raise DKNRuntimeError("type(x) requiere exactamente un argumento.")
            return self._type_name(args[0])

        if name == "dump_memory":
            if len(args) != 0:
                raise DKNRuntimeError("dump_memory() no recibe argumentos.")
            dump = self.heap.dump_state()
            print(dump)
            return None

        if name == "id":
            if len(args) != 1:
                raise DKNRuntimeError("id(x) requiere exactamente un argumento.")
            raw = arg_exprs[0].getText().strip() if arg_exprs else ""
            ptr = self._lookup_ptr(raw) if raw else None
            if ptr is not None:
                return ptr
            return hex(id(args[0]))

        if name == "dir":
            if len(args) != 1:
                raise DKNRuntimeError("dir(x) requiere exactamente un argumento.")
            return sorted(dir(args[0]))

        if name == "help":
            if len(args) != 1:
                raise DKNRuntimeError("help(x) requiere exactamente un argumento.")
            doc = getattr(args[0], "__doc__", None)
            return doc.strip() if isinstance(doc, str) else "No hay documentación disponible."

        if name == "repr":
            if len(args) != 1:
                raise DKNRuntimeError("repr(x) requiere exactamente un argumento.")
            return repr(args[0])

        if name == "str":
            if len(args) != 1:
                raise DKNRuntimeError("str(x) requiere exactamente un argumento.")
            return str(args[0])

        if name == "print":
            if len(args) != 1:
                raise DKNRuntimeError("print(x) requiere exactamente un argumento.")
            print(args[0])
            return None

        if name == "read":
            if len(args) != 1:
                raise DKNRuntimeError("read(ruta) requiere exactamente un argumento (string).")
            path = self._require_str(args[0], "ruta")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
            except OSError as e:
                raise DKNRuntimeError(f"No se pudo leer el archivo: {e}") from e

        if name == "write":
            if len(args) != 2:
                raise DKNRuntimeError("write(ruta, contenido) requiere exactamente dos argumentos (strings).")
            path = self._require_str(args[0], "ruta")
            content = self._require_str(args[1], "contenido")
            try:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(content)
            except OSError as e:
                raise DKNRuntimeError(f"No se pudo escribir el archivo: {e}") from e
            return None

        if name == "load_csv":
            if len(args) != 1:
                raise DKNRuntimeError("load_csv(ruta) requiere exactamente un argumento (string).")
            path = self._require_str(args[0], "ruta")
            try:
                mat = dataDKN.load_csv_matrix(path, self._bump_instruction)
            except ValueError as e:
                raise DKNRuntimeError(f"load_csv: {e}") from e
            return mat

        if name == "get_col":
            if len(args) != 2:
                raise DKNRuntimeError("get_col(matriz, indice) requiere exactamente dos argumentos.")
            mat, idx_raw = args[0], args[1]
            j = self._coerce_int_index(idx_raw, "get_col")
            try:
                col = matrixDKN.get_column(mat, j)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e
            for _ in col:
                self._bump_instruction()
            return col

        if name == "set_col":
            if len(args) != 3:
                raise DKNRuntimeError("set_col(matriz, indice, vector) requiere exactamente tres argumentos.")
            mat, idx_raw, vec = args[0], args[1], args[2]
            j = self._coerce_int_index(idx_raw, "set_col")
            try:
                out = matrixDKN.set_column(mat, j, vec)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e
            dims = matrixDKN.matrix_dimensions(out)
            if dims is not None:
                rows, cols = dims
                for _ in range(rows * cols):
                    self._bump_instruction()
            return out

        if name == "sum":
            if len(args) != 1:
                raise DKNRuntimeError("sum(x) requiere exactamente un argumento (lista o matriz).")
            try:
                return mathDKN.dk_sum(args[0], self._bump_instruction)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e

        if name == "mean":
            if len(args) != 1:
                raise DKNRuntimeError("mean(x) requiere exactamente un argumento (lista o matriz).")
            try:
                return mathDKN.dk_mean(args[0], self._bump_instruction)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e

        if name == "min":
            if len(args) != 1:
                raise DKNRuntimeError("min(x) requiere exactamente un argumento (lista o matriz).")
            try:
                return mathDKN.dk_min(args[0], self._bump_instruction)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e

        if name == "max":
            if len(args) != 1:
                raise DKNRuntimeError("max(x) requiere exactamente un argumento (lista o matriz).")
            try:
                return mathDKN.dk_max(args[0], self._bump_instruction)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e

        if name == "normalize":
            if len(args) != 1:
                raise DKNRuntimeError("normalize(vector) requiere exactamente un argumento.")
            try:
                return mathDKN.normalize_vector(args[0], self._bump_instruction)
            except ValueError as e:
                raise DKNRuntimeError(str(e)) from e

        # ---- Métricas de Machine Learning ----

        if name == "mse":
            if len(args) != 2:
                raise DKNRuntimeError("mse(y_real, y_pred) requiere dos argumentos (listas).")
            y_real = self._ml_vector(args[0], "mse", "y_real")
            y_pred = self._ml_vector(args[1], "mse", "y_pred")
            if len(y_real) != len(y_pred):
                raise DKNRuntimeError("mse: y_real y y_pred deben tener la misma longitud.")
            total = 0.0
            for i in range(len(y_real)):
                self._bump_instruction()
                diff = y_real[i] - y_pred[i]
                total += diff * diff
            return total / len(y_real)

        if name == "exactitud":
            if len(args) != 2:
                raise DKNRuntimeError("exactitud(y_real, y_pred) requiere dos argumentos (listas).")
            y_real = self._ml_binary(args[0], "exactitud", "y_real")
            y_pred = self._ml_binary(args[1], "exactitud", "y_pred")
            if len(y_real) != len(y_pred):
                raise DKNRuntimeError("exactitud: y_real y y_pred deben tener la misma longitud.")
            aciertos = 0
            for i in range(len(y_real)):
                self._bump_instruction()
                if y_real[i] == y_pred[i]:
                    aciertos += 1
            return aciertos / len(y_real)

        if name == "matriz_confusion":
            if len(args) != 2:
                raise DKNRuntimeError("matriz_confusion(y_real, y_pred) requiere dos argumentos (listas).")
            y_real = self._ml_binary(args[0], "matriz_confusion", "y_real")
            y_pred = self._ml_binary(args[1], "matriz_confusion", "y_pred")
            if len(y_real) != len(y_pred):
                raise DKNRuntimeError("matriz_confusion: y_real y y_pred deben tener la misma longitud.")
            tn = fp = fn = tp = 0
            for i in range(len(y_real)):
                self._bump_instruction()
                real, pred = y_real[i], y_pred[i]
                if real == 0 and pred == 0:
                    tn += 1
                elif real == 0 and pred == 1:
                    fp += 1
                elif real == 1 and pred == 0:
                    fn += 1
                else:
                    tp += 1
            c00, c01 = f"[{tn}]", f"[{fp}]"
            c10, c11 = f"[{fn}]", f"[{tp}]"
            h0, h1 = "Pred: 0", "Pred: 1"
            w0 = max(len(h0), len(c00), len(c10))
            w1 = max(len(h1), len(c01), len(c11))
            sangria = " " * len("Real 0: ")
            print("[Matriz de Confusion]")
            print(f"{sangria}{h0.center(w0)}  {h1.center(w1)}")
            print(f"Real 0: {c00.center(w0)}  {c01.center(w1)}")
            print(f"Real 1: {c10.center(w0)}  {c11.center(w1)}")
            return None

        # ---- Gráficos en texto (Canvas ASCII) ----

        if name == "graficar_dispersion":
            if len(args) != 2:
                raise DKNRuntimeError("graficar_dispersion(X, Y) requiere dos argumentos (listas).")
            X = self._ml_vector(args[0], "graficar_dispersion", "X")
            Y = self._ml_vector(args[1], "graficar_dispersion", "Y")
            if len(X) != len(Y):
                raise DKNRuntimeError("graficar_dispersion: X e Y deben tener la misma longitud.")
            print(self._ascii_canvas(X, Y, None, title="[Grafico de Dispersion]"))
            return None

        if name == "graficar_linea":
            if len(args) != 3:
                raise DKNRuntimeError("graficar_linea(X, Y, W) requiere tres argumentos (listas).")
            X = self._ml_vector(args[0], "graficar_linea", "X")
            Y = self._ml_vector(args[1], "graficar_linea", "Y")
            W = self._ml_vector(args[2], "graficar_linea", "W")
            if len(X) != len(Y):
                raise DKNRuntimeError("graficar_linea: X e Y deben tener la misma longitud.")
            if len(W) < 2:
                raise DKNRuntimeError("graficar_linea: W debe tener al menos 2 elementos (W[0]=bias, W[1]=peso).")
            print(self._ascii_canvas(X, Y, W, title="[Grafico de Linea / Regresion]"))
            return None

        if name not in self.functions:
            raise DKNRuntimeError(f"Error Semántico: La función '{name}' no está definida.")

        fd = self.functions[name]
        params = fd["params"]
        if len(args) != len(params):
            raise DKNRuntimeError(
                f"Error Semántico: La función '{name}' espera {len(params)} argumento(s), se recibieron {len(args)}."
            )

        saved_ret = self._returned
        saved_val = self.return_value
        old_scopes = self.scopes
        # Aislamiento de función: solo alcance global + alcance local propio.
        self.scopes = [old_scopes[0], {}]
        self._returned = False
        self.return_value = None
        result = None
        try:
            for pname, val in zip(params, args):
                self._assign_var(pname, val)
            for st in fd["statements"]:
                if self._returned:
                    break
                self.visit(st)
            result = self.return_value if self._returned else None
        finally:
            self.scopes = old_scopes
            self._returned = saved_ret
            self.return_value = saved_val
        return result

    def visitSinFunc(self, ctx):
        return mathDKN.sin(self._require_number(self.visit(ctx.expr())))

    def visitCosFunc(self, ctx):
        return mathDKN.cos(self._require_number(self.visit(ctx.expr())))

    def visitTanFunc(self, ctx):
        try:
            return mathDKN.tan(self._require_number(self.visit(ctx.expr())))
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitTanhFunc(self, ctx):
        try:
            return mathDKN.tanh(self._require_number(self.visit(ctx.expr())))
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitSqrtFunc(self, ctx):
        try:
            return mathDKN.sqrt(self._require_number(self.visit(ctx.expr())))
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitRootFunc(self, ctx):
        try:
            x = self._require_number(self.visit(ctx.expr(0)))
            y = self._require_number(self.visit(ctx.expr(1)))
            return mathDKN.root(x, y)
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitLogFunc(self, ctx):
        try:
            return mathDKN.log(self._require_number(self.visit(ctx.expr())))
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitLog10Func(self, ctx):
        try:
            return mathDKN.log10(self._require_number(self.visit(ctx.expr())))
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitAbsFunc(self, ctx):
        return mathDKN.abs(self._require_number(self.visit(ctx.expr())))

    def visitFloorFunc(self, ctx):
        return mathDKN.floor(self._require_number(self.visit(ctx.expr())))

    def visitCeilFunc(self, ctx):
        return mathDKN.ceil(self._require_number(self.visit(ctx.expr())))

    def visitMatrixTrans(self, ctx):
        m = self.visit(ctx.expr())
        try:
            return matrixDKN.matrix_transpose(m)
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitMatrixInv(self, ctx):
        m = self.visit(ctx.expr())
        try:
            return matrixDKN.matrix_inv(m)
        except ValueError as e:
            raise DKNRuntimeError(str(e))

    def visitStackPop(self, ctx):
        name = ctx.VARIABLE().getText()
        lst = self._lookup_var_optional(name)
        if lst is None or not isinstance(lst, list):
            raise DKNRuntimeError(f"Error Semántico: La pila '{name}' no existe o no es una lista.")
        if not lst:
            raise DKNRuntimeError(f"Error: La pila '{name}' está vacía.")
        return lst.pop()

    def visitQueueDequeue(self, ctx):
        name = ctx.VARIABLE().getText()
        lst = self._lookup_var_optional(name)
        if lst is None or not isinstance(lst, list):
            raise DKNRuntimeError(f"Error Semántico: La cola '{name}' no existe o no es una lista.")
        if not lst:
            raise DKNRuntimeError(f"Error: La cola '{name}' está vacía.")
        return lst.pop(0)

    def visitListLiteral(self, ctx):
        values = []
        for e in ctx.expr():
            values.append(self.visit(e))
        return values

    def _dict_key(self, raw):
        """Valida y normaliza una clave de diccionario (string o número entero)."""
        if isinstance(raw, bool):
            raise DKNRuntimeError("Clave de diccionario inválida: no se admiten booleanos.")
        if isinstance(raw, str):
            return raw
        if isinstance(raw, int):
            return raw
        if isinstance(raw, float):
            # Permite claves numéricas pero normaliza enteros exactos.
            return int(raw) if raw.is_integer() else raw
        raise DKNRuntimeError(
            "Clave de diccionario inválida: solo se admiten strings o números."
        )

    def visitDictLiteral(self, ctx):
        """Construye un diccionario propio (tabla hash) {clave: valor, ...}."""
        result = {}
        for entry in ctx.dictEntry():
            self._bump_instruction()
            key = self._dict_key(self.visit(entry.expr(0)))
            value = self.visit(entry.expr(1))
            result[key] = value
        return result

    def visitUnaryMinus(self, ctx):
        v = self._require_number(self.visit(ctx.expr()))
        return -v

    def visitPiConst(self, ctx):
        return mathDKN.PI

    def visitEConst(self, ctx):
        return mathDKN.E

    def visitInfConst(self, ctx):
        return mathDKN.INF

    def visitSumaResta(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if self._is_matrix(left) or self._is_matrix(right):
            if not (self._is_matrix(left) and self._is_matrix(right)):
                raise DKNRuntimeError("Error de Dominio: No se puede sumar/restar matriz con escalar.")
            try:
                return matrixDKN.matrix_add(left, right) if op == '+' else matrixDKN.matrix_sub(left, right)
            except ValueError as e:
                raise DKNRuntimeError(str(e))
        if op == '+':
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            if isinstance(left, str) != isinstance(right, str):
                raise DKNRuntimeError(
                    "No se pueden sumar tipos diferentes: un número y un string."
                )
        left = self._require_number(left)
        right = self._require_number(right)
        res = left + right if op == '+' else left - right
        return self._reject_nan(res)

    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            if self._is_matrix(left) or self._is_matrix(right):
                try:
                    if self._is_matrix(left) and self._is_matrix(right):
                        return matrixDKN.matrix_mul(left, right)
                    if self._is_matrix(left) and isinstance(right, (int, float)):
                        return matrixDKN.matrix_scalar_mul(left, right)
                    if self._is_matrix(right) and isinstance(left, (int, float)):
                        return matrixDKN.matrix_scalar_mul(right, left)
                    raise DKNRuntimeError("Error de Dominio: multiplicación inválida con matrices.")
                except ValueError as e:
                    raise DKNRuntimeError(str(e))
            left = self._require_number(left)
            right = self._require_number(right)
            return self._reject_nan(left * right)
        if op == '/':
            if self._is_matrix(left) or self._is_matrix(right):
                raise DKNRuntimeError("Error de Dominio: división no soportada para matrices.")
            left = self._require_number(left)
            right = self._require_number(right)
            if right == 0:
                raise DKNRuntimeError("Imposible dividir entre 0.")
            try:
                return self._reject_nan(left / right)
            except OverflowError:
                raise DKNRuntimeError("Error de Desbordamiento: El resultado es demasiado grande para ser procesado.")
        # '%'
        if self._is_matrix(left) or self._is_matrix(right):
            raise DKNRuntimeError("Error de Dominio: módulo no soportado para matrices.")
        left = self._require_number(left)
        right = self._require_number(right)
        if right == 0:
            raise DKNRuntimeError("Imposible calcular módulo entre 0.")
        return self._reject_nan(left % right)

    def visitComparacion(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text if hasattr(ctx, "op") else ctx.getChild(1).getText()

        if self._is_matrix(left) or self._is_matrix(right):
            raise DKNRuntimeError("Error de Dominio: comparación no soportada para matrices.")

        if op in ("==", "!="):
            res = (left == right)
            return (not res) if op == "!=" else res

        left = self._require_number(left)
        right = self._require_number(right)
        if op == "<":
            return left < right
        if op == ">":
            return left > right
        if op == "<=":
            return left <= right
        if op == ">=":
            return left >= right
        raise DKNRuntimeError(f"Operador de comparación inválido: {op}")

    def visitPotencia(self, ctx):
        self._bump_instruction()
        left = self._require_number(self.visit(ctx.expr(0)))
        right = self._require_number(self.visit(ctx.expr(1)))
        if isinstance(left, bool) or isinstance(right, bool):
            raise DKNRuntimeError("Error de Tipo: la potencia requiere operandos numéricos reales.")
        if left == 0 and right == 0:
            raise DKNRuntimeError("Error matemático: 0 ^ 0 es indeterminado.")
        if left == 0 and right < 0:
            raise DKNRuntimeError("Error matemático: 0 elevado a exponente negativo (división por cero).")
        try:
            out = left ** right
            if isinstance(out, complex):
                raise DKNRuntimeError(
                    "Error de Dominio: la potencia produce un resultado complejo (fuera de los reales)."
                )
            return self._reject_nan(out)
        except OverflowError:
            raise DKNRuntimeError("Error de Desbordamiento: El resultado es demasiado grande para ser procesado.")

    # Llamado por el parser cuando existe la etiqueta # PrintCommand.
    def visitPrintCommand(self, ctx):
        if self._returned:
            return None
        self._bump_instruction()
        val = self.visit(self._expr0(ctx))
        print(val)
        return None

    # Llamado por el parser cuando existe la etiqueta # ReturnStmt.
    def visitReturnStmt(self, ctx):
        self._bump_instruction()
        self.return_value = self.visit(self._expr0(ctx))
        self._returned = True
        return self.return_value

    def visitReturnVoid(self, ctx):
        self._bump_instruction()
        self.return_value = None
        self._returned = True
        return None

    # Alias en inglés por si se usa esa etiqueta en la gramática.
    def visitAssignment(self, ctx):
        return self.visitAsignacion(ctx)

    # Llamado cuando existe la etiqueta # multiplicacion y division (ctx.op = token * / %).
    def visitMultiplicacionYDivision(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text if hasattr(ctx, 'op') else ctx.getChild(1).getText()
        if op == '*':
            return left * right
        if op == '/':
            return left / right if right != 0 else 0
        return left % right if right != 0 else 0

    # Alias para gramática con etiqueta # muldiv.
    def visitMulDiv(self, ctx):
        return self.visitMultiplicacionYDivision(ctx)

    # Llamado cuando existe la etiqueta # suma y resta.
    def visitSumaYResta(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text if hasattr(ctx, 'op') else ctx.getChild(1).getText()
        if op == '+':
            return left + right
        return left - right

    # (visitPotencia ya está implementado arriba con validaciones)

def run(code: str, *, heap_slots: int | None = None, instruction_limit: int = 1_000_000):
    """Analiza y ejecuta código del DSL."""
    code_for_lexer = _normalize_return_keyword(code)
    input_stream = InputStream(code_for_lexer)
    lexer = grammarDKNLexer(input_stream)
    lexer_err = CollectingErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_err)

    stream = CommonTokenStream(lexer)
    stream.fill()

    # Error léxico específico: identificador inválido (empieza con número).
    for tok in stream.tokens:
        if tok.type == grammarDKNLexer.INVALID_ID:
            raise DKNParseError(
                f"Identificador inválido '{tok.text}' en L{tok.line}:{tok.column}. "
                "Un identificador no puede empezar con número."
            )

    parser = grammarDKNParser(stream)
    parser_err = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_err)

    tree = parser.program()
    visitor = EvalVisitor(heap_slots=heap_slots, instruction_limit=instruction_limit)
    if lexer_err.errors or parser_err.errors:
        errors = lexer_err.errors + parser_err.errors
        raise DKNParseError("\n".join(errors))

    try:
        visitor.visit(tree)
        return visitor.return_value if visitor._returned else None
    except (DKNRuntimeError, DKNMemoryError):
        raise


def _normalize_return_keyword(code: str) -> str:
    """Valida palabras clave y bloquea el uso de `return`."""
    i = 0
    n = len(code)
    out = []
    in_string = False
    in_line_comment = False

    while i < n:
        ch = code[i]

        if in_line_comment:
            out.append(ch)
            if ch == '\n':
                in_line_comment = False
            i += 1
            continue

        if in_string:
            out.append(ch)
            if ch == '\\' and i + 1 < n:
                out.append(code[i + 1])
                i += 2
                continue
            if ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
            continue

        if ch == '/' and i + 1 < n and code[i + 1] == '/':
            in_line_comment = True
            out.append(ch)
            out.append(code[i + 1])
            i += 2
            continue

        if ch.isalpha() or ch == '_':
            start = i
            i += 1
            while i < n and (code[i].isalnum() or code[i] == '_'):
                i += 1
            word = code[start:i]
            if word == "return":
                raise DKNParseError(
                    "La palabra clave 'return' ya no es válida. Usa 'retornar'."
                )
            out.append(word)
            continue

        out.append(ch)
        i += 1

    return "".join(out)


def start_repl():
    """Bucle de consola interactiva (REPL)."""
    print("Escribe código y una línea vacía para ejecutar. Ejemplo: 3 + 5 ;")
    print("Escribe 'exit' o 'quit' para salir.")
    buf = []
    try:
        while True:
            line = input("> " if not buf else "")
            if line.strip().lower() in ("exit", "quit"):
                print("Saliendo de DKNexus... ¡Adiós!")
                return
            if line == "" and buf:
                try:
                    ret = run("\n".join(buf))
                    if ret is not None:
                        print(ret)
                    print(">>> Ejecutado.")
                except (DKNParseError, DKNRuntimeError, DKNMemoryError) as e:
                    print("Error:", e)
                buf = []
            elif line == "":
                continue
            else:
                buf.append(line)
    except EOFError:
        if buf:
            run("\n".join(buf))
    except KeyboardInterrupt:
        print("\nSaliendo de DKNexus... ¡Adiós!")
        return


def main():
    # Todo entra por input(), sin sys.argv.
    try:
        print("--- DKNexus DSL Interpreter ---")
        print("Para ejecutar un archivo, escribe la ruta (ej: prueba.dkn).")
        print("Para entrar a la consola interactiva, presiona Enter.")

        path = input(">> ").strip()

        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    codigo = f.read()
                print(f"\n--- Ejecutando: {path} ---")
                ret = run(codigo)
                if ret is not None:
                    print(ret)
                print("--- Fin de ejecución ---\n")
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo '{path}'.")
            except (DKNParseError, DKNRuntimeError, DKNMemoryError) as e:
                print("Error durante la ejecución:", e)
            except Exception as e:
                print("Ocurrió un error inesperado:", e)
        else:
            start_repl()
    except KeyboardInterrupt:
        print("\nSaliendo de DKNexus... ¡Adiós!")
        return


if __name__ == "__main__":
    main()
