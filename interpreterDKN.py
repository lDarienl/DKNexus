#!/usr/bin/env python3
"""
Intérprete del DSL DKNexus usando ANTLR4 y patrón Visitor.
Ejecutar desde el directorio del proyecto (donde están los .py generados por ANTLR).
"""

import mathDKN
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

    def __init__(self):
        self.variables = {}
        self._returned = False
        self.return_value = None

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

    def _reject_nan(self, value):
        # NaN es el único valor que no es igual a sí mismo en Python
        if isinstance(value, float) and value != value:
            raise DKNRuntimeError("Operación inválida: El resultado es un valor indeterminado (NaN).")
        return value

    def visitProgram(self, ctx):
        for st in ctx.statement():
            if self._returned:
                break
            self.visit(st)
        return None

    def visitStatement(self, ctx):
        # Con alternativas etiquetadas (#PrintExpr, #IfStmt, etc.) ANTLR llamará
        # a los métodos específicos. Este método queda como fallback.
        return self.visitChildren(ctx)

    # ---- Statement visitors (etiquetas actuales en grammarDKN.g4) ----
    def visitPrintExpr(self, ctx):
        if self._returned:
            return None
        val = self.visit(self._expr0(ctx))
        if val is not None:
            print(val)
        return None

    def visitAsignacion(self, ctx):
        if self._returned:
            return None
        name = ctx.VARIABLE().getText()
        value = self.visit(self._expr0(ctx))
        self.variables[name] = value
        return value

    def visitIfStmt(self, ctx):
        if self._returned:
            return None
        cond = self.visit(self._expr0(ctx))
        if cond:
            for st in ctx.statement():
                if self._returned:
                    break
                self.visit(st)
        return None

    def visitWhileStmt(self, ctx):
        if self._returned:
            return None
        # expr ')' '{' statement+ '}'
        while self.visit(self._expr0(ctx)):
            for st in ctx.statement():
                if self._returned:
                    break
                self.visit(st)
            if self._returned:
                break
        return None

    def visitForStmt(self, ctx):
        if self._returned:
            return None
        # for '(' expr ';' expr ';' expr ')' '{' statement+ '}'
        self.visit(ctx.expr(0))  # init
        while self.visit(ctx.expr(1)):
            for st in ctx.statement():
                if self._returned:
                    break
                self.visit(st)
            if self._returned:
                break
            self.visit(ctx.expr(2))  # update
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
            if name not in self.variables:
                raise DKNRuntimeError(f"Error Semántico: La variable '{name}' no ha sido declarada.")
            return self.variables[name]
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
        if name not in self.variables:
            raise DKNRuntimeError(f"Error Semántico: La variable '{name}' no ha sido declarada.")
        return self.variables[name]

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

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
        left = self._require_number(self.visit(ctx.expr(0)))
        right = self._require_number(self.visit(ctx.expr(1)))
        op = ctx.op.text
        res = left + right if op == '+' else left - right
        return self._reject_nan(res)

    def visitMulDivMod(self, ctx):
        left = self._require_number(self.visit(ctx.expr(0)))
        right = self._require_number(self.visit(ctx.expr(1)))
        op = ctx.op.text
        if op == '*':
            return self._reject_nan(left * right)
        if op == '/':
            if right == 0:
                raise DKNRuntimeError("Imposible dividir entre 0.")
            try:
                return self._reject_nan(left / right)
            except OverflowError:
                raise DKNRuntimeError("Error de Desbordamiento: El resultado es demasiado grande para ser procesado.")
        # '%'
        if right == 0:
            raise DKNRuntimeError("Imposible calcular módulo entre 0.")
        return self._reject_nan(left % right)

    def visitPotencia(self, ctx):
        left = self._require_number(self.visit(ctx.expr(0)))
        right = self._require_number(self.visit(ctx.expr(1)))
        if left == 0 and right == 0:
            raise DKNRuntimeError("Error matemático: 0 ^ 0 es indeterminado.")
        if left == 0 and right < 0:
            raise DKNRuntimeError("Error matemático: 0 elevado a exponente negativo (división por cero).")
        try:
            return self._reject_nan(left ** right)
        except OverflowError:
            raise DKNRuntimeError("Error de Desbordamiento: El resultado es demasiado grande para ser procesado.")

    # Llamado por el parser cuando existe la etiqueta # PrintCommand.
    def visitPrintCommand(self, ctx):
        val = self.visit(self._expr0(ctx))
        print(val)
        return None

    # Llamado por el parser cuando existe la etiqueta # ReturnStmt.
    def visitReturnStmt(self, ctx):
        self.return_value = self.visit(self._expr0(ctx))
        self._returned = True
        return self.return_value

    def visitReturnVoid(self, ctx):
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

    # Llamado cuando existe la etiqueta # potencia.
    def visitPotencia(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

def run(code: str):
    """Analiza y ejecuta código del DSL."""
    input_stream = InputStream(code)
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
    visitor = EvalVisitor()
    if lexer_err.errors or parser_err.errors:
        errors = lexer_err.errors + parser_err.errors
        raise DKNParseError("\n".join(errors))

    try:
        visitor.visit(tree)
        return visitor.return_value if visitor._returned else None
    except DKNRuntimeError:
        raise


def start_repl():
    """Bucle de consola interactiva (REPL)."""
    print("Escribe código y una línea vacía para ejecutar. Ejemplo: 3 + 5 ;")
    buf = []
    try:
        while True:
            line = input("> " if not buf else "")
            if line == "" and buf:
                try:
                    ret = run("\n".join(buf))
                    if ret is not None:
                        print(ret)
                except (DKNParseError, DKNRuntimeError) as e:
                    print("Error:", e)
                buf = []
            elif line == "":
                continue
            else:
                buf.append(line)
    except EOFError:
        if buf:
            run("\n".join(buf))


def main():
    print("--- DKNexus DSL Interpreter ---")
    path = input("Ingrese la ruta del archivo .dkn o presione Enter para consola: ")

    if path.strip():
        try:
            with open(path.strip(), 'r', encoding='utf-8') as f:
                try:
                    run(f.read())
                except (DKNParseError, DKNRuntimeError) as e:
                    print("Error:", e)
        except Exception as e:
            print("Error al abrir el archivo:", e)
    else:
        start_repl()


if __name__ == "__main__":
    main()
