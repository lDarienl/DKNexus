# Generated from grammarDKN.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarDKNParser import grammarDKNParser
else:
    from grammarDKNParser import grammarDKNParser

# This class defines a complete generic visitor for a parse tree produced by grammarDKNParser.

class grammarDKNVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarDKNParser#program.
    def visitProgram(self, ctx:grammarDKNParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#statement.
    def visitStatement(self, ctx:grammarDKNParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#expr.
    def visitExpr(self, ctx:grammarDKNParser.ExprContext):
        return self.visitChildren(ctx)



del grammarDKNParser