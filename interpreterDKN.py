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

    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitStatement(self, ctx):
        # asignacion: VARIABLE '=' expr ';' (detectar antes que expr para no imprimir)
        if ctx.VARIABLE() and ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == '=':
            name = ctx.VARIABLE().getText()
            value = self.visit(ctx.expr())
            self.variables[name] = value
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

    def visitExpr(self, ctx):
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

    # Llamado por el parser cuando existe la etiqueta # asignacion (tras regenerar con antlr4).
    def visitAsignacion(self, ctx):
        name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())  # ctx.expr() es lista; usar expr(0)
        self.variables[name] = value
        return value

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
