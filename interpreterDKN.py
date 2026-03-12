#!/usr/bin/env python3
"""
Intérprete del DSL DKNexus usando ANTLR4 y patrón Visitor.
Ejecutar desde el directorio del proyecto (donde están los .py generados por ANTLR).
"""

import mathDKN
from antlr4 import InputStream, CommonTokenStream
from grammarDKNLexer import grammarDKNLexer
from grammarDKNParser import grammarDKNParser
from grammarDKNVisitor import grammarDKNVisitor


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

    def visitProgram(self, ctx):
        for st in ctx.statement():
            if self._returned:
                break
            self.visit(st)
        return None

    def visitStatement(self, ctx):
        if self._returned:
            return None

        # asignacion: VARIABLE '=' expr ';' (detectar antes que expr para no imprimir)
        if ctx.VARIABLE() and ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == '=':
            name = ctx.VARIABLE().getText()
            value = self.visit(self._expr0(ctx))
            self.variables[name] = value
            return None

        # print(expr);
        if ctx.getChildCount() >= 5 and ctx.getChild(0).getText() == 'print':
            val = self.visit(self._expr0(ctx))
            print(val)
            return None

        # return expr;
        if ctx.getChildCount() >= 3 and ctx.getChild(0).getText() == 'return':
            self.return_value = self.visit(self._expr0(ctx))
            self._returned = True
            return None

        # expr ';' (imprimir expresión)
        if ctx.expr():
            val = self.visit(ctx.expr(0))
            if val is not None:
                print(val)
        elif ctx.getChild(0).getText() == 'if':
            cond = self.visit(ctx.expr(0))
            if cond:
                for st in ctx.statement():
                    self.visit(st)
        elif ctx.getChild(0).getText() == 'for':
            self.visit(ctx.expr(0))  # init
            while self.visit(ctx.expr(1)):
                for st in ctx.statement():
                    self.visit(st)
                self.visit(ctx.expr(2))  # update
        elif ctx.getChild(0).getText() == 'while':
            while self.visit(ctx.expr(0)):
                for st in ctx.statement():
                    self.visit(st)
        return None

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
            return self.variables.get(name, 0)
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
        return self.variables.get(name, 0)

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitSinFunc(self, ctx):
        return mathDKN.sin(self.visit(ctx.expr()))

    def visitCosFunc(self, ctx):
        return mathDKN.cos(self.visit(ctx.expr()))

    def visitTanFunc(self, ctx):
        return mathDKN.tan(self.visit(ctx.expr()))

    def visitSumaResta(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left + right if op == '+' else left - right

    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        if op == '/':
            return left / right if right != 0 else 0
        return left % right if right != 0 else 0

    def visitPotencia(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

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
    stream = CommonTokenStream(lexer)
    parser = grammarDKNParser(stream)
    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)


def start_repl():
    """Bucle de consola interactiva (REPL)."""
    print("Escribe código y una línea vacía para ejecutar. Ejemplo: 3 + 5 ;")
    buf = []
    try:
        while True:
            line = input("> " if not buf else "")
            if line == "" and buf:
                run("\n".join(buf))
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
                run(f.read())
        except Exception as e:
            print("Error al abrir el archivo:", e)
    else:
        start_repl()


if __name__ == "__main__":
    main()
