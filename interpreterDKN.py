#!/usr/bin/env python3
"""
Intérprete del DSL DKNexus usando ANTLR4 y patrón Visitor.
Ejecutar desde el directorio del proyecto (donde están los .py generados por ANTLR).
"""

import math
import sys
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
        # expr ';' | if | for | while
        if ctx.expr():
            val = self.visit(ctx.expr())
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
                return math.sin(val)
            if first == 'cos':
                return math.cos(val)
            if first == 'tan':
                return math.tan(val)
        return None


def run(code: str):
    """Analiza y ejecuta código del DSL."""
    input_stream = InputStream(code)
    lexer = grammarDKNLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammarDKNParser(stream)
    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            run(f.read())
    else:
        print("DKNexus DSL (solo ANTLR4). Escribe código y una línea vacía para ejecutar.")
        print("Ejemplo: 3 + 5 ;")
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


if __name__ == "__main__":
    main()
