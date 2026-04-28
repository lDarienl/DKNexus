# Generated from grammar/grammarDKN.g4 by ANTLR 4.13.2
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
        4,1,56,263,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,26,
        8,2,10,2,12,2,29,9,2,3,2,31,8,2,1,2,1,2,1,2,4,2,36,8,2,11,2,12,2,
        37,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,84,8,3,11,
        3,12,3,85,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,100,
        8,3,11,3,12,3,101,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,112,8,3,11,
        3,12,3,113,1,3,1,3,3,3,118,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,5,4,211,8,4,10,4,12,4,214,9,4,3,4,216,8,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,229,8,4,10,4,12,4,232,9,4,3,
        4,234,8,4,1,4,1,4,3,4,238,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,258,8,4,10,4,12,4,261,
        9,4,1,4,0,1,8,5,0,2,4,6,8,0,3,1,0,18,20,2,0,16,16,21,21,1,0,22,27,
        310,0,11,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,6,117,1,0,0,0,8,237,1,
        0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,
        14,1,0,0,0,14,1,1,0,0,0,15,18,3,4,2,0,16,18,3,6,3,0,17,15,1,0,0,
        0,17,16,1,0,0,0,18,3,1,0,0,0,19,20,5,51,0,0,20,21,5,55,0,0,21,30,
        5,1,0,0,22,27,5,55,0,0,23,24,5,2,0,0,24,26,5,55,0,0,25,23,1,0,0,
        0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,31,1,0,0,0,29,27,
        1,0,0,0,30,22,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,3,0,0,
        33,35,5,4,0,0,34,36,3,6,3,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,
        0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,5,0,0,40,5,1,0,0,0,41,
        42,5,6,0,0,42,43,5,1,0,0,43,44,3,8,4,0,44,45,5,3,0,0,45,46,5,7,0,
        0,46,118,1,0,0,0,47,48,5,8,0,0,48,49,3,8,4,0,49,50,5,7,0,0,50,118,
        1,0,0,0,51,52,5,8,0,0,52,118,5,7,0,0,53,54,5,9,0,0,54,55,5,1,0,0,
        55,56,5,55,0,0,56,57,5,2,0,0,57,58,3,8,4,0,58,59,5,3,0,0,59,60,5,
        7,0,0,60,118,1,0,0,0,61,62,5,10,0,0,62,63,5,1,0,0,63,64,5,55,0,0,
        64,65,5,2,0,0,65,66,3,8,4,0,66,67,5,3,0,0,67,68,5,7,0,0,68,118,1,
        0,0,0,69,70,3,8,4,0,70,71,5,7,0,0,71,118,1,0,0,0,72,73,5,55,0,0,
        73,74,5,11,0,0,74,75,3,8,4,0,75,76,5,7,0,0,76,118,1,0,0,0,77,78,
        5,12,0,0,78,79,5,1,0,0,79,80,3,8,4,0,80,81,5,3,0,0,81,83,5,4,0,0,
        82,84,3,6,3,0,83,82,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,
        0,0,0,86,87,1,0,0,0,87,88,5,5,0,0,88,118,1,0,0,0,89,90,5,13,0,0,
        90,91,5,1,0,0,91,92,3,8,4,0,92,93,5,7,0,0,93,94,3,8,4,0,94,95,5,
        7,0,0,95,96,3,8,4,0,96,97,5,3,0,0,97,99,5,4,0,0,98,100,3,6,3,0,99,
        98,1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,103,
        1,0,0,0,103,104,5,5,0,0,104,118,1,0,0,0,105,106,5,14,0,0,106,107,
        5,1,0,0,107,108,3,8,4,0,108,109,5,3,0,0,109,111,5,4,0,0,110,112,
        3,6,3,0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,
        1,0,0,0,114,115,1,0,0,0,115,116,5,5,0,0,116,118,1,0,0,0,117,41,1,
        0,0,0,117,47,1,0,0,0,117,51,1,0,0,0,117,53,1,0,0,0,117,61,1,0,0,
        0,117,69,1,0,0,0,117,72,1,0,0,0,117,77,1,0,0,0,117,89,1,0,0,0,117,
        105,1,0,0,0,118,7,1,0,0,0,119,120,6,4,-1,0,120,121,5,15,0,0,121,
        238,3,8,4,33,122,123,5,16,0,0,123,238,3,8,4,32,124,125,5,1,0,0,125,
        126,3,8,4,0,126,127,5,3,0,0,127,238,1,0,0,0,128,129,5,55,0,0,129,
        130,5,11,0,0,130,238,3,8,4,24,131,132,5,30,0,0,132,133,5,1,0,0,133,
        134,3,8,4,0,134,135,5,3,0,0,135,238,1,0,0,0,136,137,5,31,0,0,137,
        138,5,1,0,0,138,139,3,8,4,0,139,140,5,3,0,0,140,238,1,0,0,0,141,
        142,5,32,0,0,142,143,5,1,0,0,143,144,3,8,4,0,144,145,5,3,0,0,145,
        238,1,0,0,0,146,147,5,33,0,0,147,148,5,1,0,0,148,149,3,8,4,0,149,
        150,5,3,0,0,150,238,1,0,0,0,151,152,5,34,0,0,152,153,5,1,0,0,153,
        154,3,8,4,0,154,155,5,3,0,0,155,238,1,0,0,0,156,157,5,35,0,0,157,
        158,5,1,0,0,158,159,3,8,4,0,159,160,5,2,0,0,160,161,3,8,4,0,161,
        162,5,3,0,0,162,238,1,0,0,0,163,164,5,36,0,0,164,165,5,1,0,0,165,
        166,3,8,4,0,166,167,5,3,0,0,167,238,1,0,0,0,168,169,5,37,0,0,169,
        170,5,1,0,0,170,171,3,8,4,0,171,172,5,3,0,0,172,238,1,0,0,0,173,
        174,5,38,0,0,174,175,5,1,0,0,175,176,3,8,4,0,176,177,5,3,0,0,177,
        238,1,0,0,0,178,179,5,39,0,0,179,180,5,1,0,0,180,181,3,8,4,0,181,
        182,5,3,0,0,182,238,1,0,0,0,183,184,5,40,0,0,184,185,5,1,0,0,185,
        186,3,8,4,0,186,187,5,3,0,0,187,238,1,0,0,0,188,189,5,41,0,0,189,
        190,5,1,0,0,190,191,3,8,4,0,191,192,5,3,0,0,192,238,1,0,0,0,193,
        194,5,42,0,0,194,195,5,1,0,0,195,196,3,8,4,0,196,197,5,3,0,0,197,
        238,1,0,0,0,198,199,5,43,0,0,199,200,5,1,0,0,200,201,5,55,0,0,201,
        238,5,3,0,0,202,203,5,44,0,0,203,204,5,1,0,0,204,205,5,55,0,0,205,
        238,5,3,0,0,206,215,5,45,0,0,207,212,3,8,4,0,208,209,5,2,0,0,209,
        211,3,8,4,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,
        213,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,215,207,1,0,0,0,215,
        216,1,0,0,0,216,217,1,0,0,0,217,238,5,46,0,0,218,238,5,52,0,0,219,
        238,5,53,0,0,220,238,5,54,0,0,221,238,5,47,0,0,222,238,5,48,0,0,
        223,224,5,55,0,0,224,233,5,1,0,0,225,230,3,8,4,0,226,227,5,2,0,0,
        227,229,3,8,4,0,228,226,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,
        230,231,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,233,225,1,0,0,0,
        233,234,1,0,0,0,234,235,1,0,0,0,235,238,5,3,0,0,236,238,5,55,0,0,
        237,119,1,0,0,0,237,122,1,0,0,0,237,124,1,0,0,0,237,128,1,0,0,0,
        237,131,1,0,0,0,237,136,1,0,0,0,237,141,1,0,0,0,237,146,1,0,0,0,
        237,151,1,0,0,0,237,156,1,0,0,0,237,163,1,0,0,0,237,168,1,0,0,0,
        237,173,1,0,0,0,237,178,1,0,0,0,237,183,1,0,0,0,237,188,1,0,0,0,
        237,193,1,0,0,0,237,198,1,0,0,0,237,202,1,0,0,0,237,206,1,0,0,0,
        237,218,1,0,0,0,237,219,1,0,0,0,237,220,1,0,0,0,237,221,1,0,0,0,
        237,222,1,0,0,0,237,223,1,0,0,0,237,236,1,0,0,0,238,259,1,0,0,0,
        239,240,10,30,0,0,240,241,5,17,0,0,241,258,3,8,4,31,242,243,10,29,
        0,0,243,244,7,0,0,0,244,258,3,8,4,30,245,246,10,28,0,0,246,247,7,
        1,0,0,247,258,3,8,4,29,248,249,10,27,0,0,249,250,7,2,0,0,250,258,
        3,8,4,28,251,252,10,26,0,0,252,253,5,28,0,0,253,258,3,8,4,27,254,
        255,10,25,0,0,255,256,5,29,0,0,256,258,3,8,4,26,257,239,1,0,0,0,
        257,242,1,0,0,0,257,245,1,0,0,0,257,248,1,0,0,0,257,251,1,0,0,0,
        257,254,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,
        260,9,1,0,0,0,261,259,1,0,0,0,16,13,17,27,30,37,85,101,113,117,212,
        215,230,233,237,257,259
    ]

class grammarDKNParser ( Parser ):

    grammarFileName = "grammarDKN.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'print'", 
                     "';'", "'return'", "'push'", "'enqueue'", "'='", "'if'", 
                     "'for'", "'while'", "'not'", "'-'", "'^'", "'*'", "'/'", 
                     "'%'", "'+'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "'and'", "'or'", "'sin'", "'cos'", "'tan'", 
                     "'tanh'", "'sqrt'", "'root'", "'log'", "'log10'", "'abs'", 
                     "'floor'", "'ceil'", "'trans'", "'inv'", "'pop'", "'dequeue'", 
                     "'['", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'function'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "STRING", 
                      "INVALID_ID", "LINE_COMMENT", "FUNCTION", "PI", "EULER", 
                      "INF", "VARIABLE", "WS" ]

    RULE_program = 0
    RULE_programItem = 1
    RULE_functionDef = 2
    RULE_statement = 3
    RULE_expr = 4

    ruleNames =  [ "program", "programItem", "functionDef", "statement", 
                   "expr" ]

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
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    NUMBER=47
    STRING=48
    INVALID_ID=49
    LINE_COMMENT=50
    FUNCTION=51
    PI=52
    EULER=53
    INF=54
    VARIABLE=55
    WS=56

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

        def programItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ProgramItemContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ProgramItemContext,i)


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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.programItem()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70298374359873346) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarDKNParser.RULE_programItem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ItemStmtContext(ProgramItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ProgramItemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(grammarDKNParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemStmt" ):
                return visitor.visitItemStmt(self)
            else:
                return visitor.visitChildren(self)


    class ItemFuncContext(ProgramItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ProgramItemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionDef(self):
            return self.getTypedRuleContext(grammarDKNParser.FunctionDefContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemFunc" ):
                return visitor.visitItemFunc(self)
            else:
                return visitor.visitChildren(self)



    def programItem(self):

        localctx = grammarDKNParser.ProgramItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programItem)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                localctx = grammarDKNParser.ItemFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.functionDef()
                pass
            elif token in [1, 6, 8, 9, 10, 12, 13, 14, 15, 16, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 52, 53, 54, 55]:
                localctx = grammarDKNParser.ItemStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarDKNParser.RULE_functionDef

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionDefRuleContext(FunctionDefContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.FunctionDefContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNCTION(self):
            return self.getToken(grammarDKNParser.FUNCTION, 0)
        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarDKNParser.VARIABLE)
            else:
                return self.getToken(grammarDKNParser.VARIABLE, i)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefRule" ):
                return visitor.visitFunctionDefRule(self)
            else:
                return visitor.visitChildren(self)



    def functionDef(self):

        localctx = grammarDKNParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            localctx = grammarDKNParser.FunctionDefRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(grammarDKNParser.FUNCTION)
            self.state = 20
            self.match(grammarDKNParser.VARIABLE)
            self.state = 21
            self.match(grammarDKNParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 22
                self.match(grammarDKNParser.VARIABLE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 23
                    self.match(grammarDKNParser.T__1)
                    self.state = 24
                    self.match(grammarDKNParser.VARIABLE)
                    self.state = 29
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 32
            self.match(grammarDKNParser.T__2)
            self.state = 33
            self.match(grammarDKNParser.T__3)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.statement()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68046574546188098) != 0)):
                    break

            self.state = 39
            self.match(grammarDKNParser.T__4)
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
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = grammarDKNParser.PrintCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(grammarDKNParser.T__5)
                self.state = 42
                self.match(grammarDKNParser.T__0)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(grammarDKNParser.T__2)
                self.state = 45
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 2:
                localctx = grammarDKNParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(grammarDKNParser.T__7)
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 3:
                localctx = grammarDKNParser.ReturnVoidContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(grammarDKNParser.T__7)
                self.state = 52
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 4:
                localctx = grammarDKNParser.StackPushStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.match(grammarDKNParser.T__8)
                self.state = 54
                self.match(grammarDKNParser.T__0)
                self.state = 55
                self.match(grammarDKNParser.VARIABLE)
                self.state = 56
                self.match(grammarDKNParser.T__1)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(grammarDKNParser.T__2)
                self.state = 59
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 5:
                localctx = grammarDKNParser.QueueEnqueueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(grammarDKNParser.T__9)
                self.state = 62
                self.match(grammarDKNParser.T__0)
                self.state = 63
                self.match(grammarDKNParser.VARIABLE)
                self.state = 64
                self.match(grammarDKNParser.T__1)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(grammarDKNParser.T__2)
                self.state = 67
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 6:
                localctx = grammarDKNParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 7:
                localctx = grammarDKNParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.match(grammarDKNParser.VARIABLE)
                self.state = 73
                self.match(grammarDKNParser.T__10)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(grammarDKNParser.T__6)
                pass

            elif la_ == 8:
                localctx = grammarDKNParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.match(grammarDKNParser.T__11)
                self.state = 78
                self.match(grammarDKNParser.T__0)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(grammarDKNParser.T__2)
                self.state = 81
                self.match(grammarDKNParser.T__3)
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 82
                    self.statement()
                    self.state = 85 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68046574546188098) != 0)):
                        break

                self.state = 87
                self.match(grammarDKNParser.T__4)
                pass

            elif la_ == 9:
                localctx = grammarDKNParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.match(grammarDKNParser.T__12)
                self.state = 90
                self.match(grammarDKNParser.T__0)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(grammarDKNParser.T__6)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(grammarDKNParser.T__6)
                self.state = 95
                self.expr(0)
                self.state = 96
                self.match(grammarDKNParser.T__2)
                self.state = 97
                self.match(grammarDKNParser.T__3)
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 98
                    self.statement()
                    self.state = 101 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68046574546188098) != 0)):
                        break

                self.state = 103
                self.match(grammarDKNParser.T__4)
                pass

            elif la_ == 10:
                localctx = grammarDKNParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 105
                self.match(grammarDKNParser.T__13)
                self.state = 106
                self.match(grammarDKNParser.T__0)
                self.state = 107
                self.expr(0)
                self.state = 108
                self.match(grammarDKNParser.T__2)
                self.state = 109
                self.match(grammarDKNParser.T__3)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 110
                    self.statement()
                    self.state = 113 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68046574546188098) != 0)):
                        break

                self.state = 115
                self.match(grammarDKNParser.T__4)
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


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


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


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
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


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(grammarDKNParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
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


    class ComparacionContext(ExprContext):

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
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
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


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarDKNParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(grammarDKNParser.VARIABLE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarDKNParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarDKNParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = grammarDKNParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 120
                self.match(grammarDKNParser.T__14)
                self.state = 121
                self.expr(33)
                pass

            elif la_ == 2:
                localctx = grammarDKNParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(grammarDKNParser.T__15)
                self.state = 123
                self.expr(32)
                pass

            elif la_ == 3:
                localctx = grammarDKNParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(grammarDKNParser.T__0)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 4:
                localctx = grammarDKNParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(grammarDKNParser.VARIABLE)
                self.state = 129
                self.match(grammarDKNParser.T__10)
                self.state = 130
                self.expr(24)
                pass

            elif la_ == 5:
                localctx = grammarDKNParser.SinFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(grammarDKNParser.T__29)
                self.state = 132
                self.match(grammarDKNParser.T__0)
                self.state = 133
                self.expr(0)
                self.state = 134
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 6:
                localctx = grammarDKNParser.CosFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(grammarDKNParser.T__30)
                self.state = 137
                self.match(grammarDKNParser.T__0)
                self.state = 138
                self.expr(0)
                self.state = 139
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 7:
                localctx = grammarDKNParser.TanFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(grammarDKNParser.T__31)
                self.state = 142
                self.match(grammarDKNParser.T__0)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 8:
                localctx = grammarDKNParser.TanhFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(grammarDKNParser.T__32)
                self.state = 147
                self.match(grammarDKNParser.T__0)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 9:
                localctx = grammarDKNParser.SqrtFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(grammarDKNParser.T__33)
                self.state = 152
                self.match(grammarDKNParser.T__0)
                self.state = 153
                self.expr(0)
                self.state = 154
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 10:
                localctx = grammarDKNParser.RootFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(grammarDKNParser.T__34)
                self.state = 157
                self.match(grammarDKNParser.T__0)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(grammarDKNParser.T__1)
                self.state = 160
                self.expr(0)
                self.state = 161
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 11:
                localctx = grammarDKNParser.LogFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(grammarDKNParser.T__35)
                self.state = 164
                self.match(grammarDKNParser.T__0)
                self.state = 165
                self.expr(0)
                self.state = 166
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 12:
                localctx = grammarDKNParser.Log10FuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(grammarDKNParser.T__36)
                self.state = 169
                self.match(grammarDKNParser.T__0)
                self.state = 170
                self.expr(0)
                self.state = 171
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 13:
                localctx = grammarDKNParser.AbsFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.match(grammarDKNParser.T__37)
                self.state = 174
                self.match(grammarDKNParser.T__0)
                self.state = 175
                self.expr(0)
                self.state = 176
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 14:
                localctx = grammarDKNParser.FloorFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.match(grammarDKNParser.T__38)
                self.state = 179
                self.match(grammarDKNParser.T__0)
                self.state = 180
                self.expr(0)
                self.state = 181
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 15:
                localctx = grammarDKNParser.CeilFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(grammarDKNParser.T__39)
                self.state = 184
                self.match(grammarDKNParser.T__0)
                self.state = 185
                self.expr(0)
                self.state = 186
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 16:
                localctx = grammarDKNParser.MatrixTransContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.match(grammarDKNParser.T__40)
                self.state = 189
                self.match(grammarDKNParser.T__0)
                self.state = 190
                self.expr(0)
                self.state = 191
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 17:
                localctx = grammarDKNParser.MatrixInvContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.match(grammarDKNParser.T__41)
                self.state = 194
                self.match(grammarDKNParser.T__0)
                self.state = 195
                self.expr(0)
                self.state = 196
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 18:
                localctx = grammarDKNParser.StackPopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.match(grammarDKNParser.T__42)
                self.state = 199
                self.match(grammarDKNParser.T__0)
                self.state = 200
                self.match(grammarDKNParser.VARIABLE)
                self.state = 201
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 19:
                localctx = grammarDKNParser.QueueDequeueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                self.match(grammarDKNParser.T__43)
                self.state = 203
                self.match(grammarDKNParser.T__0)
                self.state = 204
                self.match(grammarDKNParser.VARIABLE)
                self.state = 205
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 20:
                localctx = grammarDKNParser.ListLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 206
                self.match(grammarDKNParser.T__44)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68046574546157570) != 0):
                    self.state = 207
                    self.expr(0)
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 208
                        self.match(grammarDKNParser.T__1)
                        self.state = 209
                        self.expr(0)
                        self.state = 214
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 217
                self.match(grammarDKNParser.T__45)
                pass

            elif la_ == 21:
                localctx = grammarDKNParser.PiConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(grammarDKNParser.PI)
                pass

            elif la_ == 22:
                localctx = grammarDKNParser.EConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 219
                self.match(grammarDKNParser.EULER)
                pass

            elif la_ == 23:
                localctx = grammarDKNParser.InfConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 220
                self.match(grammarDKNParser.INF)
                pass

            elif la_ == 24:
                localctx = grammarDKNParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 221
                self.match(grammarDKNParser.NUMBER)
                pass

            elif la_ == 25:
                localctx = grammarDKNParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.match(grammarDKNParser.STRING)
                pass

            elif la_ == 26:
                localctx = grammarDKNParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 223
                self.match(grammarDKNParser.VARIABLE)
                self.state = 224
                self.match(grammarDKNParser.T__0)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68046574546157570) != 0):
                    self.state = 225
                    self.expr(0)
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 226
                        self.match(grammarDKNParser.T__1)
                        self.state = 227
                        self.expr(0)
                        self.state = 232
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 235
                self.match(grammarDKNParser.T__2)
                pass

            elif la_ == 27:
                localctx = grammarDKNParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                self.match(grammarDKNParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = grammarDKNParser.PotenciaContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 239
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 240
                        self.match(grammarDKNParser.T__16)
                        self.state = 241
                        self.expr(31)
                        pass

                    elif la_ == 2:
                        localctx = grammarDKNParser.MulDivModContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 242
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 243
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 244
                        self.expr(30)
                        pass

                    elif la_ == 3:
                        localctx = grammarDKNParser.SumaRestaContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 246
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expr(29)
                        pass

                    elif la_ == 4:
                        localctx = grammarDKNParser.ComparacionContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 249
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(28)
                        pass

                    elif la_ == 5:
                        localctx = grammarDKNParser.AndExprContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 252
                        self.match(grammarDKNParser.T__27)
                        self.state = 253
                        self.expr(27)
                        pass

                    elif la_ == 6:
                        localctx = grammarDKNParser.OrExprContext(self, grammarDKNParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 254
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 255
                        self.match(grammarDKNParser.T__28)
                        self.state = 256
                        self.expr(26)
                        pass

             
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 25)
         




