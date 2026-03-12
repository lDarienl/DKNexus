# Generated from grammarDKN.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,206,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,54,8,1,11,1,12,1,55,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,70,8,1,11,1,12,1,
        71,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,82,8,1,11,1,12,1,83,1,1,1,
        1,3,1,88,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,176,8,2,10,2,12,2,179,9,
        2,3,2,181,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,190,8,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,201,8,2,10,2,12,2,204,9,2,1,2,0,1,
        4,3,0,2,4,0,2,1,0,16,18,1,0,19,20,243,0,7,1,0,0,0,2,87,1,0,0,0,4,
        189,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,1,1,0,0,0,11,12,5,1,0,0,12,13,5,2,0,0,13,14,3,4,2,0,14,
        15,5,3,0,0,15,16,5,4,0,0,16,88,1,0,0,0,17,18,5,5,0,0,18,19,3,4,2,
        0,19,20,5,4,0,0,20,88,1,0,0,0,21,22,5,5,0,0,22,88,5,4,0,0,23,24,
        5,6,0,0,24,25,5,2,0,0,25,26,5,45,0,0,26,27,5,7,0,0,27,28,3,4,2,0,
        28,29,5,3,0,0,29,30,5,4,0,0,30,88,1,0,0,0,31,32,5,8,0,0,32,33,5,
        2,0,0,33,34,5,45,0,0,34,35,5,7,0,0,35,36,3,4,2,0,36,37,5,3,0,0,37,
        38,5,4,0,0,38,88,1,0,0,0,39,40,3,4,2,0,40,41,5,4,0,0,41,88,1,0,0,
        0,42,43,5,45,0,0,43,44,5,9,0,0,44,45,3,4,2,0,45,46,5,4,0,0,46,88,
        1,0,0,0,47,48,5,10,0,0,48,49,5,2,0,0,49,50,3,4,2,0,50,51,5,3,0,0,
        51,53,5,11,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,
        0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,12,0,0,58,88,1,0,0,0,59,
        60,5,13,0,0,60,61,5,2,0,0,61,62,3,4,2,0,62,63,5,4,0,0,63,64,3,4,
        2,0,64,65,5,4,0,0,65,66,3,4,2,0,66,67,5,3,0,0,67,69,5,11,0,0,68,
        70,3,2,1,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,
        0,72,73,1,0,0,0,73,74,5,12,0,0,74,88,1,0,0,0,75,76,5,14,0,0,76,77,
        5,2,0,0,77,78,3,4,2,0,78,79,5,3,0,0,79,81,5,11,0,0,80,82,3,2,1,0,
        81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,
        0,0,0,85,86,5,12,0,0,86,88,1,0,0,0,87,11,1,0,0,0,87,17,1,0,0,0,87,
        21,1,0,0,0,87,23,1,0,0,0,87,31,1,0,0,0,87,39,1,0,0,0,87,42,1,0,0,
        0,87,47,1,0,0,0,87,59,1,0,0,0,87,75,1,0,0,0,88,3,1,0,0,0,89,90,6,
        2,-1,0,90,91,5,20,0,0,91,190,3,4,2,24,92,93,5,2,0,0,93,94,3,4,2,
        0,94,95,5,3,0,0,95,190,1,0,0,0,96,97,5,21,0,0,97,98,5,2,0,0,98,99,
        3,4,2,0,99,100,5,3,0,0,100,190,1,0,0,0,101,102,5,22,0,0,102,103,
        5,2,0,0,103,104,3,4,2,0,104,105,5,3,0,0,105,190,1,0,0,0,106,107,
        5,23,0,0,107,108,5,2,0,0,108,109,3,4,2,0,109,110,5,3,0,0,110,190,
        1,0,0,0,111,112,5,24,0,0,112,113,5,2,0,0,113,114,3,4,2,0,114,115,
        5,3,0,0,115,190,1,0,0,0,116,117,5,25,0,0,117,118,5,2,0,0,118,119,
        3,4,2,0,119,120,5,3,0,0,120,190,1,0,0,0,121,122,5,26,0,0,122,123,
        5,2,0,0,123,124,3,4,2,0,124,125,5,7,0,0,125,126,3,4,2,0,126,127,
        5,3,0,0,127,190,1,0,0,0,128,129,5,27,0,0,129,130,5,2,0,0,130,131,
        3,4,2,0,131,132,5,3,0,0,132,190,1,0,0,0,133,134,5,28,0,0,134,135,
        5,2,0,0,135,136,3,4,2,0,136,137,5,3,0,0,137,190,1,0,0,0,138,139,
        5,29,0,0,139,140,5,2,0,0,140,141,3,4,2,0,141,142,5,3,0,0,142,190,
        1,0,0,0,143,144,5,30,0,0,144,145,5,2,0,0,145,146,3,4,2,0,146,147,
        5,3,0,0,147,190,1,0,0,0,148,149,5,31,0,0,149,150,5,2,0,0,150,151,
        3,4,2,0,151,152,5,3,0,0,152,190,1,0,0,0,153,154,5,32,0,0,154,155,
        5,2,0,0,155,156,3,4,2,0,156,157,5,3,0,0,157,190,1,0,0,0,158,159,
        5,33,0,0,159,160,5,2,0,0,160,161,3,4,2,0,161,162,5,3,0,0,162,190,
        1,0,0,0,163,164,5,34,0,0,164,165,5,2,0,0,165,166,5,45,0,0,166,190,
        5,3,0,0,167,168,5,35,0,0,168,169,5,2,0,0,169,170,5,45,0,0,170,190,
        5,3,0,0,171,180,5,36,0,0,172,177,3,4,2,0,173,174,5,7,0,0,174,176,
        3,4,2,0,175,173,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,180,172,1,0,0,0,180,181,
        1,0,0,0,181,182,1,0,0,0,182,190,5,37,0,0,183,190,5,42,0,0,184,190,
        5,43,0,0,185,190,5,44,0,0,186,190,5,38,0,0,187,190,5,39,0,0,188,
        190,5,45,0,0,189,89,1,0,0,0,189,92,1,0,0,0,189,96,1,0,0,0,189,101,
        1,0,0,0,189,106,1,0,0,0,189,111,1,0,0,0,189,116,1,0,0,0,189,121,
        1,0,0,0,189,128,1,0,0,0,189,133,1,0,0,0,189,138,1,0,0,0,189,143,
        1,0,0,0,189,148,1,0,0,0,189,153,1,0,0,0,189,158,1,0,0,0,189,163,
        1,0,0,0,189,167,1,0,0,0,189,171,1,0,0,0,189,183,1,0,0,0,189,184,
        1,0,0,0,189,185,1,0,0,0,189,186,1,0,0,0,189,187,1,0,0,0,189,188,
        1,0,0,0,190,202,1,0,0,0,191,192,10,27,0,0,192,193,5,15,0,0,193,201,
        3,4,2,28,194,195,10,26,0,0,195,196,7,0,0,0,196,201,3,4,2,27,197,
        198,10,25,0,0,198,199,7,1,0,0,199,201,3,4,2,26,200,191,1,0,0,0,200,
        194,1,0,0,0,200,197,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,5,1,0,0,0,204,202,1,0,0,0,10,9,55,71,83,87,177,180,
        189,200,202
    ]

class grammarDKNParser ( Parser ):

    grammarFileName = "grammarDKN.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "';'", "'return'", 
                     "'push'", "','", "'enqueue'", "'='", "'if'", "'{'", 
                     "'}'", "'for'", "'while'", "'^'", "'*'", "'/'", "'%'", 
                     "'+'", "'-'", "'sin'", "'cos'", "'tan'", "'tanh'", 
                     "'sqrt'", "'root'", "'log'", "'log10'", "'abs'", "'floor'", 
                     "'ceil'", "'trans'", "'inv'", "'pop'", "'dequeue'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "STRING", "INVALID_ID", 
                      "LINE_COMMENT", "PI", "EULER", "INF", "VARIABLE", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2

    ruleNames =  [ "program", "statement", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    NUMBER=38
    STRING=39
    INVALID_ID=40
    LINE_COMMENT=41
    PI=42
    EULER=43
    INF=44
    VARIABLE=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarDKNParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grammarDKNParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.statement()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 66932769318246) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarDKNParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReturnVoidContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnVoid" ):
                return visitor.visitReturnVoid(self)
            else:
                return visitor.visitChildren(self)


    class StackPushStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStackPushStmt" ):
                return visitor.visitStackPushStmt(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class QueueEnqueueStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueueEnqueueStmt" ):
                return visitor.visitQueueEnqueueStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class PrintCommandContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintCommand" ):
                return visitor.visitPrintCommand(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = grammarDKNParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = grammarDKNParser.PrintCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(grammarDKNParser.T__0)
                self.state = 12
                self.match(grammarDKNParser.T__1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(grammarDKNParser.T__2)
                self.state = 15
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 2:
                localctx = grammarDKNParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(grammarDKNParser.T__4)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 3:
                localctx = grammarDKNParser.ReturnVoidContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(grammarDKNParser.T__4)
                self.state = 22
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 4:
                localctx = grammarDKNParser.StackPushStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.match(grammarDKNParser.T__5)
                self.state = 24
                self.match(grammarDKNParser.T__1)
                self.state = 25
                self.match(grammarDKNParser.VARIABLE)
                self.state = 26
                self.match(grammarDKNParser.T__6)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(grammarDKNParser.T__2)
                self.state = 29
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 5:
                localctx = grammarDKNParser.QueueEnqueueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(grammarDKNParser.T__7)
                self.state = 32
                self.match(grammarDKNParser.T__1)
                self.state = 33
                self.match(grammarDKNParser.VARIABLE)
                self.state = 34
                self.match(grammarDKNParser.T__6)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(grammarDKNParser.T__2)
                self.state = 37
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 6:
                localctx = grammarDKNParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 7:
                localctx = grammarDKNParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 42
                self.match(grammarDKNParser.VARIABLE)
                self.state = 43
                self.match(grammarDKNParser.T__8)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(grammarDKNParser.T__3)
                pass

            elif la_ == 8:
                localctx = grammarDKNParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 47
                self.match(grammarDKNParser.T__9)
                self.state = 48
                self.match(grammarDKNParser.T__1)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(grammarDKNParser.T__2)
                self.state = 51
                self.match(grammarDKNParser.T__10)
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 52
                    self.statement()
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 66932769318246) != 0)):
                        break

                self.state = 57
                self.match(grammarDKNParser.T__11)
                pass

            elif la_ == 9:
                localctx = grammarDKNParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.match(grammarDKNParser.T__12)
                self.state = 60
                self.match(grammarDKNParser.T__1)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(grammarDKNParser.T__3)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(grammarDKNParser.T__3)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(grammarDKNParser.T__2)
                self.state = 67
                self.match(grammarDKNParser.T__10)
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 68
                    self.statement()
                    self.state = 71 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 66932769318246) != 0)):
                        break

                self.state = 73
                self.match(grammarDKNParser.T__11)
                pass

            elif la_ == 10:
                localctx = grammarDKNParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 75
                self.match(grammarDKNParser.T__13)
                self.state = 76
                self.match(grammarDKNParser.T__1)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(grammarDKNParser.T__2)
                self.state = 79
                self.match(grammarDKNParser.T__10)
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 80
                    self.statement()
                    self.state = 83 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 66932769318246) != 0)):
                        break

                self.state = 85
                self.match(grammarDKNParser.T__11)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarDKNParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TanhFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanhFunc" ):
                return visitor.visitTanhFunc(self)
            else:
                return visitor.visitChildren(self)


    class RootFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRootFunc" ):
                return visitor.visitRootFunc(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class PiConstContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PI(self):
            return self.getToken(grammarDKNParser.PI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiConst" ):
                return visitor.visitPiConst(self)
            else:
                return visitor.visitChildren(self)


    class SqrtFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqrtFunc" ):
                return visitor.visitSqrtFunc(self)
            else:
                return visitor.visitChildren(self)


    class FloorFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloorFunc" ):
                return visitor.visitFloorFunc(self)
            else:
                return visitor.visitChildren(self)


    class CeilFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCeilFunc" ):
                return visitor.visitCeilFunc(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)


    class AbsFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbsFunc" ):
                return visitor.visitAbsFunc(self)
            else:
                return visitor.visitChildren(self)


    class MatrixInvContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixInv" ):
                return visitor.visitMatrixInv(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class LogFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogFunc" ):
                return visitor.visitLogFunc(self)
            else:
                return visitor.visitChildren(self)


    class SinFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinFunc" ):
                return visitor.visitSinFunc(self)
            else:
                return visitor.visitChildren(self)


    class Log10FuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog10Func" ):
                return visitor.visitLog10Func(self)
            else:
                return visitor.visitChildren(self)


    class TanFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(grammarDKNParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class MatrixTransContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixTrans" ):
                return visitor.visitMatrixTrans(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class CosFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
            else:
                return visitor.visitChildren(self)


    class ListLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(grammarDKNParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StackPopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStackPop" ):
                return visitor.visitStackPop(self)
            else:
                return visitor.visitChildren(self)


    class InfConstContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INF(self):
            return self.getToken(grammarDKNParser.INF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfConst" ):
                return visitor.visitInfConst(self)
            else:
                return visitor.visitChildren(self)


    class PotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)


    class EConstContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EULER(self):
            return self.getToken(grammarDKNParser.EULER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEConst" ):
                return visitor.visitEConst(self)
            else:
                return visitor.visitChildren(self)


    class QueueDequeueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueueDequeue" ):
                return visitor.visitQueueDequeue(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarDKNParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = grammarDKNParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 90
                self.match(grammarDKNParser.T__19)
                self.state = 91
                self.expr(24)
                pass
            elif token in [2]:
                localctx = grammarDKNParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(grammarDKNParser.T__1)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [21]:
                localctx = grammarDKNParser.SinFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(grammarDKNParser.T__20)
                self.state = 97
                self.match(grammarDKNParser.T__1)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [22]:
                localctx = grammarDKNParser.CosFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(grammarDKNParser.T__21)
                self.state = 102
                self.match(grammarDKNParser.T__1)
                self.state = 103
                self.expr(0)
                self.state = 104
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [23]:
                localctx = grammarDKNParser.TanFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(grammarDKNParser.T__22)
                self.state = 107
                self.match(grammarDKNParser.T__1)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [24]:
                localctx = grammarDKNParser.TanhFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(grammarDKNParser.T__23)
                self.state = 112
                self.match(grammarDKNParser.T__1)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [25]:
                localctx = grammarDKNParser.SqrtFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(grammarDKNParser.T__24)
                self.state = 117
                self.match(grammarDKNParser.T__1)
                self.state = 118
                self.expr(0)
                self.state = 119
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [26]:
                localctx = grammarDKNParser.RootFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(grammarDKNParser.T__25)
                self.state = 122
                self.match(grammarDKNParser.T__1)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(grammarDKNParser.T__6)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [27]:
                localctx = grammarDKNParser.LogFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(grammarDKNParser.T__26)
                self.state = 129
                self.match(grammarDKNParser.T__1)
                self.state = 130
                self.expr(0)
                self.state = 131
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [28]:
                localctx = grammarDKNParser.Log10FuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(grammarDKNParser.T__27)
                self.state = 134
                self.match(grammarDKNParser.T__1)
                self.state = 135
                self.expr(0)
                self.state = 136
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [29]:
                localctx = grammarDKNParser.AbsFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(grammarDKNParser.T__28)
                self.state = 139
                self.match(grammarDKNParser.T__1)
                self.state = 140
                self.expr(0)
                self.state = 141
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [30]:
                localctx = grammarDKNParser.FloorFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(grammarDKNParser.T__29)
                self.state = 144
                self.match(grammarDKNParser.T__1)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [31]:
                localctx = grammarDKNParser.CeilFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(grammarDKNParser.T__30)
                self.state = 149
                self.match(grammarDKNParser.T__1)
                self.state = 150
                self.expr(0)
                self.state = 151
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [32]:
                localctx = grammarDKNParser.MatrixTransContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(grammarDKNParser.T__31)
                self.state = 154
                self.match(grammarDKNParser.T__1)
                self.state = 155
                self.expr(0)
                self.state = 156
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [33]:
                localctx = grammarDKNParser.MatrixInvContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(grammarDKNParser.T__32)
                self.state = 159
                self.match(grammarDKNParser.T__1)
                self.state = 160
                self.expr(0)
                self.state = 161
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [34]:
                localctx = grammarDKNParser.StackPopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(grammarDKNParser.T__33)
                self.state = 164
                self.match(grammarDKNParser.T__1)
                self.state = 165
                self.match(grammarDKNParser.VARIABLE)
                self.state = 166
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [35]:
                localctx = grammarDKNParser.QueueDequeueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 167
                self.match(grammarDKNParser.T__34)
                self.state = 168
                self.match(grammarDKNParser.T__1)
                self.state = 169
                self.match(grammarDKNParser.VARIABLE)
                self.state = 170
                self.match(grammarDKNParser.T__2)
                pass
            elif token in [36]:
                localctx = grammarDKNParser.ListLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                self.match(grammarDKNParser.T__35)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66932769292292) != 0):
                    self.state = 172
                    self.expr(0)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==7:
                        self.state = 173
                        self.match(grammarDKNParser.T__6)
                        self.state = 174
                        self.expr(0)
                        self.state = 179
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 182
                self.match(grammarDKNParser.T__36)
                pass
            elif token in [42]:
                localctx = grammarDKNParser.PiConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(grammarDKNParser.PI)
                pass
            elif token in [43]:
                localctx = grammarDKNParser.EConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 184
                self.match(grammarDKNParser.EULER)
                pass
            elif token in [44]:
                localctx = grammarDKNParser.InfConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(grammarDKNParser.INF)
                pass
            elif token in [38]:
                localctx = grammarDKNParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 186
                self.match(grammarDKNParser.NUMBER)
                pass
            elif token in [39]:
                localctx = grammarDKNParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(grammarDKNParser.STRING)
                pass
            elif token in [45]:
                localctx = grammarDKNParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.match(grammarDKNParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 200
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = grammarDKNParser.PotenciaContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 192
                        self.match(grammarDKNParser.T__14)
                        self.state = 193
                        self.expr(28)
                        pass

                    elif la_ == 2:
                        localctx = grammarDKNParser.MulDivModContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 195
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        self.expr(27)
                        pass

                    elif la_ == 3:
                        localctx = grammarDKNParser.SumaRestaContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 198
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 199
                        self.expr(26)
                        pass

             
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 25)
         




