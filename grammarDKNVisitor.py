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


    # Visit a parse tree produced by grammarDKNParser#PrintCommand.
    def visitPrintCommand(self, ctx:grammarDKNParser.PrintCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#ReturnStmt.
    def visitReturnStmt(self, ctx:grammarDKNParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#ReturnVoid.
    def visitReturnVoid(self, ctx:grammarDKNParser.ReturnVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#StackPushStmt.
    def visitStackPushStmt(self, ctx:grammarDKNParser.StackPushStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#QueueEnqueueStmt.
    def visitQueueEnqueueStmt(self, ctx:grammarDKNParser.QueueEnqueueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#PrintExpr.
    def visitPrintExpr(self, ctx:grammarDKNParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#Asignacion.
    def visitAsignacion(self, ctx:grammarDKNParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#IfStmt.
    def visitIfStmt(self, ctx:grammarDKNParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#ForStmt.
    def visitForStmt(self, ctx:grammarDKNParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#WhileStmt.
    def visitWhileStmt(self, ctx:grammarDKNParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#TanhFunc.
    def visitTanhFunc(self, ctx:grammarDKNParser.TanhFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#RootFunc.
    def visitRootFunc(self, ctx:grammarDKNParser.RootFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#Parens.
    def visitParens(self, ctx:grammarDKNParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#Var.
    def visitVar(self, ctx:grammarDKNParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#PiConst.
    def visitPiConst(self, ctx:grammarDKNParser.PiConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#SqrtFunc.
    def visitSqrtFunc(self, ctx:grammarDKNParser.SqrtFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#FloorFunc.
    def visitFloorFunc(self, ctx:grammarDKNParser.FloorFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#CeilFunc.
    def visitCeilFunc(self, ctx:grammarDKNParser.CeilFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#SumaResta.
    def visitSumaResta(self, ctx:grammarDKNParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#AbsFunc.
    def visitAbsFunc(self, ctx:grammarDKNParser.AbsFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#MatrixInv.
    def visitMatrixInv(self, ctx:grammarDKNParser.MatrixInvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#MulDivMod.
    def visitMulDivMod(self, ctx:grammarDKNParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#LogFunc.
    def visitLogFunc(self, ctx:grammarDKNParser.LogFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#SinFunc.
    def visitSinFunc(self, ctx:grammarDKNParser.SinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#Log10Func.
    def visitLog10Func(self, ctx:grammarDKNParser.Log10FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#TanFunc.
    def visitTanFunc(self, ctx:grammarDKNParser.TanFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#Num.
    def visitNum(self, ctx:grammarDKNParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#MatrixTrans.
    def visitMatrixTrans(self, ctx:grammarDKNParser.MatrixTransContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:grammarDKNParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#CosFunc.
    def visitCosFunc(self, ctx:grammarDKNParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#ListLiteral.
    def visitListLiteral(self, ctx:grammarDKNParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#StringLiteral.
    def visitStringLiteral(self, ctx:grammarDKNParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#StackPop.
    def visitStackPop(self, ctx:grammarDKNParser.StackPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#InfConst.
    def visitInfConst(self, ctx:grammarDKNParser.InfConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#Potencia.
    def visitPotencia(self, ctx:grammarDKNParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#EConst.
    def visitEConst(self, ctx:grammarDKNParser.EConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarDKNParser#QueueDequeue.
    def visitQueueDequeue(self, ctx:grammarDKNParser.QueueDequeueContext):
        return self.visitChildren(ctx)



del grammarDKNParser