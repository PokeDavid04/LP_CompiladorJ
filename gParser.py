# Generated from g.g4 by ANTLR 4.13.2
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
        4,1,30,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,3,0,26,8,0,1,0,
        3,0,29,8,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,4,2,63,8,2,11,2,12,2,64,1,2,3,2,68,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,79,8,2,10,2,12,2,82,9,2,1,3,1,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,3,8,106,8,8,1,9,1,9,5,9,110,8,9,10,9,12,9,113,
        9,9,1,9,1,9,1,9,3,9,118,8,9,1,10,1,10,3,10,122,8,10,1,11,1,11,5,
        11,126,8,11,10,11,12,11,129,9,11,1,11,0,1,4,12,0,2,4,6,8,10,12,14,
        16,18,20,22,0,4,1,0,5,19,2,0,18,18,20,21,1,0,23,24,1,0,27,29,139,
        0,33,1,0,0,0,2,45,1,0,0,0,4,67,1,0,0,0,6,83,1,0,0,0,8,85,1,0,0,0,
        10,87,1,0,0,0,12,89,1,0,0,0,14,91,1,0,0,0,16,105,1,0,0,0,18,107,
        1,0,0,0,20,121,1,0,0,0,22,123,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,
        0,25,26,1,0,0,0,26,28,1,0,0,0,27,29,3,22,11,0,28,27,1,0,0,0,28,29,
        1,0,0,0,29,30,1,0,0,0,30,32,5,1,0,0,31,25,1,0,0,0,32,35,1,0,0,0,
        33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,
        0,0,1,37,1,1,0,0,0,38,39,5,27,0,0,39,40,5,2,0,0,40,46,3,4,2,0,41,
        46,3,4,2,0,42,43,5,27,0,0,43,44,5,2,0,0,44,46,3,18,9,0,45,38,1,0,
        0,0,45,41,1,0,0,0,45,42,1,0,0,0,46,3,1,0,0,0,47,48,6,2,-1,0,48,49,
        5,3,0,0,49,50,3,4,2,0,50,51,5,4,0,0,51,68,1,0,0,0,52,53,3,8,4,0,
        53,54,3,4,2,6,54,68,1,0,0,0,55,56,3,6,3,0,56,57,3,12,6,0,57,58,3,
        4,2,4,58,68,1,0,0,0,59,60,5,27,0,0,60,68,3,4,2,3,61,63,3,20,10,0,
        62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,68,1,
        0,0,0,66,68,5,27,0,0,67,47,1,0,0,0,67,52,1,0,0,0,67,55,1,0,0,0,67,
        59,1,0,0,0,67,62,1,0,0,0,67,66,1,0,0,0,68,80,1,0,0,0,69,70,10,7,
        0,0,70,71,3,6,3,0,71,72,3,4,2,7,72,79,1,0,0,0,73,74,10,5,0,0,74,
        75,3,6,3,0,75,76,3,10,5,0,76,77,3,4,2,5,77,79,1,0,0,0,78,69,1,0,
        0,0,78,73,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,5,
        1,0,0,0,82,80,1,0,0,0,83,84,7,0,0,0,84,7,1,0,0,0,85,86,7,1,0,0,86,
        9,1,0,0,0,87,88,5,22,0,0,88,11,1,0,0,0,89,90,7,2,0,0,90,13,1,0,0,
        0,91,92,5,25,0,0,92,15,1,0,0,0,93,94,3,4,2,0,94,95,3,6,3,0,95,106,
        1,0,0,0,96,106,3,8,4,0,97,98,3,4,2,0,98,99,3,6,3,0,99,100,3,10,5,
        0,100,106,1,0,0,0,101,102,3,6,3,0,102,103,3,12,6,0,103,106,1,0,0,
        0,104,106,5,27,0,0,105,93,1,0,0,0,105,96,1,0,0,0,105,97,1,0,0,0,
        105,101,1,0,0,0,105,104,1,0,0,0,106,17,1,0,0,0,107,111,3,16,8,0,
        108,110,3,8,4,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,
        111,112,1,0,0,0,112,117,1,0,0,0,113,111,1,0,0,0,114,115,3,14,7,0,
        115,116,3,18,9,0,116,118,1,0,0,0,117,114,1,0,0,0,117,118,1,0,0,0,
        118,19,1,0,0,0,119,122,5,28,0,0,120,122,5,29,0,0,121,119,1,0,0,0,
        121,120,1,0,0,0,122,21,1,0,0,0,123,127,5,26,0,0,124,126,7,3,0,0,
        125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,
        128,23,1,0,0,0,129,127,1,0,0,0,13,25,28,33,45,64,67,78,80,105,111,
        117,121,127
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "'=:'", "'('", "')'", "'+'", 
                     "'-'", "'*'", "'%'", "'^'", "'|'", "'='", "'<>'", "'<'", 
                     "'>'", "'<='", "'>='", "','", "'#'", "'{'", "']'", 
                     "'i.'", "'~'", "':'", "'/'", "'@:'", "'NB.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "NUM_NEG", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_operador_bin = 3
    RULE_operador_un = 4
    RULE_operador_bin_comb = 5
    RULE_operador_un_comb = 6
    RULE_operador_comp = 7
    RULE_funcion_simple = 8
    RULE_funcion = 9
    RULE_operand = 10
    RULE_comment = 11

    ruleNames =  [ "root", "statement", "expr", "operador_bin", "operador_un", 
                   "operador_bin_comb", "operador_un_comb", "operador_comp", 
                   "funcion_simple", "funcion", "operand", "comment" ]

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
    ID=27
    NUM=28
    NUM_NEG=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_root

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrelContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(gParser.EOF, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.StatementContext)
            else:
                return self.getTypedRuleContext(gParser.StatementContext,i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.CommentContext)
            else:
                return self.getTypedRuleContext(gParser.CommentContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrel" ):
                return visitor.visitArrel(self)
            else:
                return visitor.visitChildren(self)



    def root(self):

        localctx = gParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            localctx = gParser.ArrelContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1010827242) != 0):
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 943718376) != 0):
                    self.state = 24
                    self.statement()


                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 27
                    self.comment()


                self.state = 30
                self.match(gParser.T__0)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(gParser.EOF)
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
            return gParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)


    class Asignacion_funcionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)
        def funcion(self):
            return self.getTypedRuleContext(gParser.FuncionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion_funcion" ):
                return visitor.visitAsignacion_funcion(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = gParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = gParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(gParser.ID)
                self.state = 39
                self.match(gParser.T__1)
                self.state = 40
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = gParser.ExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = gParser.Asignacion_funcionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(gParser.ID)
                self.state = 43
                self.match(gParser.T__1)
                self.state = 44
                self.funcion()
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
            return gParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class Operacion_binariaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)

        def operador_bin(self):
            return self.getTypedRuleContext(gParser.Operador_binContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacion_binaria" ):
                return visitor.visitOperacion_binaria(self)
            else:
                return visitor.visitChildren(self)


    class Llamada_funcionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion" ):
                return visitor.visitLlamada_funcion(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class OperandoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.OperandContext)
            else:
                return self.getTypedRuleContext(gParser.OperandContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperando" ):
                return visitor.visitOperando(self)
            else:
                return visitor.visitChildren(self)


    class Operacion_binaria_combinadaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)

        def operador_bin(self):
            return self.getTypedRuleContext(gParser.Operador_binContext,0)

        def operador_bin_comb(self):
            return self.getTypedRuleContext(gParser.Operador_bin_combContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacion_binaria_combinada" ):
                return visitor.visitOperacion_binaria_combinada(self)
            else:
                return visitor.visitChildren(self)


    class Operacion_unariaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador_un(self):
            return self.getTypedRuleContext(gParser.Operador_unContext,0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacion_unaria" ):
                return visitor.visitOperacion_unaria(self)
            else:
                return visitor.visitChildren(self)


    class Operacion_unaria_combinadaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador_bin(self):
            return self.getTypedRuleContext(gParser.Operador_binContext,0)

        def operador_un_comb(self):
            return self.getTypedRuleContext(gParser.Operador_un_combContext,0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacion_unaria_combinada" ):
                return visitor.visitOperacion_unaria_combinada(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = gParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 48
                self.match(gParser.T__2)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(gParser.T__3)
                pass

            elif la_ == 2:
                localctx = gParser.Operacion_unariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.operador_un()
                self.state = 53
                self.expr(6)
                pass

            elif la_ == 3:
                localctx = gParser.Operacion_unaria_combinadaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.operador_bin()
                self.state = 56
                self.operador_un_comb()
                self.state = 57
                self.expr(4)
                pass

            elif la_ == 4:
                localctx = gParser.Llamada_funcionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(gParser.ID)
                self.state = 60
                self.expr(3)
                pass

            elif la_ == 5:
                localctx = gParser.OperandoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 61
                        self.operand()

                    else:
                        raise NoViableAltException(self)
                    self.state = 64 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 6:
                localctx = gParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(gParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = gParser.Operacion_binariaContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 70
                        self.operador_bin()
                        self.state = 71
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = gParser.Operacion_binaria_combinadaContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 74
                        self.operador_bin()
                        self.state = 75
                        self.operador_bin_comb()
                        self.state = 76
                        self.expr(5)
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operador_binContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_operador_bin

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Operador_binarioContext(Operador_binContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Operador_binContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_binario" ):
                return visitor.visitOperador_binario(self)
            else:
                return visitor.visitChildren(self)



    def operador_bin(self):

        localctx = gParser.Operador_binContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operador_bin)
        self._la = 0 # Token type
        try:
            localctx = gParser.Operador_binarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048544) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_unContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_operador_un

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Operador_unarioContext(Operador_unContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Operador_unContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_unario" ):
                return visitor.visitOperador_unario(self)
            else:
                return visitor.visitChildren(self)



    def operador_un(self):

        localctx = gParser.Operador_unContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operador_un)
        self._la = 0 # Token type
        try:
            localctx = gParser.Operador_unarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3407872) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_bin_combContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_operador_bin_comb

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Operador_binario_combinacionContext(Operador_bin_combContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Operador_bin_combContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_binario_combinacion" ):
                return visitor.visitOperador_binario_combinacion(self)
            else:
                return visitor.visitChildren(self)



    def operador_bin_comb(self):

        localctx = gParser.Operador_bin_combContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operador_bin_comb)
        try:
            localctx = gParser.Operador_binario_combinacionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(gParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_un_combContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_operador_un_comb

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Operador_unario_combinacionContext(Operador_un_combContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Operador_un_combContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_unario_combinacion" ):
                return visitor.visitOperador_unario_combinacion(self)
            else:
                return visitor.visitChildren(self)



    def operador_un_comb(self):

        localctx = gParser.Operador_un_combContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operador_un_comb)
        self._la = 0 # Token type
        try:
            localctx = gParser.Operador_unario_combinacionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_operador_comp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Operador_composicionContext(Operador_compContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Operador_compContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_composicion" ):
                return visitor.visitOperador_composicion(self)
            else:
                return visitor.visitChildren(self)



    def operador_comp(self):

        localctx = gParser.Operador_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operador_comp)
        try:
            localctx = gParser.Operador_composicionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(gParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcion_simpleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_funcion_simple

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Funcion_idContext(Funcion_simpleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Funcion_simpleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion_id" ):
                return visitor.visitFuncion_id(self)
            else:
                return visitor.visitChildren(self)


    class F1Context(Funcion_simpleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Funcion_simpleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)

        def operador_bin(self):
            return self.getTypedRuleContext(gParser.Operador_binContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF1" ):
                return visitor.visitF1(self)
            else:
                return visitor.visitChildren(self)


    class F2Context(Funcion_simpleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Funcion_simpleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador_un(self):
            return self.getTypedRuleContext(gParser.Operador_unContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF2" ):
                return visitor.visitF2(self)
            else:
                return visitor.visitChildren(self)


    class F3Context(Funcion_simpleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Funcion_simpleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)

        def operador_bin(self):
            return self.getTypedRuleContext(gParser.Operador_binContext,0)

        def operador_bin_comb(self):
            return self.getTypedRuleContext(gParser.Operador_bin_combContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF3" ):
                return visitor.visitF3(self)
            else:
                return visitor.visitChildren(self)


    class F4Context(Funcion_simpleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.Funcion_simpleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador_bin(self):
            return self.getTypedRuleContext(gParser.Operador_binContext,0)

        def operador_un_comb(self):
            return self.getTypedRuleContext(gParser.Operador_un_combContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF4" ):
                return visitor.visitF4(self)
            else:
                return visitor.visitChildren(self)



    def funcion_simple(self):

        localctx = gParser.Funcion_simpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcion_simple)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = gParser.F1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.operador_bin()
                pass

            elif la_ == 2:
                localctx = gParser.F2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.operador_un()
                pass

            elif la_ == 3:
                localctx = gParser.F3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.expr(0)
                self.state = 98
                self.operador_bin()
                self.state = 99
                self.operador_bin_comb()
                pass

            elif la_ == 4:
                localctx = gParser.F4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.operador_bin()
                self.state = 102
                self.operador_un_comb()
                pass

            elif la_ == 5:
                localctx = gParser.Funcion_idContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.match(gParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_funcion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComposicionContext(FuncionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.FuncionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcion_simple(self):
            return self.getTypedRuleContext(gParser.Funcion_simpleContext,0)

        def operador_un(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.Operador_unContext)
            else:
                return self.getTypedRuleContext(gParser.Operador_unContext,i)

        def operador_comp(self):
            return self.getTypedRuleContext(gParser.Operador_compContext,0)

        def funcion(self):
            return self.getTypedRuleContext(gParser.FuncionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposicion" ):
                return visitor.visitComposicion(self)
            else:
                return visitor.visitChildren(self)



    def funcion(self):

        localctx = gParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            localctx = gParser.ComposicionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.funcion_simple()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3407872) != 0):
                self.state = 108
                self.operador_un()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 114
                self.operador_comp()
                self.state = 115
                self.funcion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_operand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Numero_negativoContext(OperandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.OperandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM_NEG(self):
            return self.getToken(gParser.NUM_NEG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero_negativo" ):
                return visitor.visitNumero_negativo(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(OperandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.OperandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(gParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)



    def operand(self):

        localctx = gParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operand)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = gParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(gParser.NUM)
                pass
            elif token in [29]:
                localctx = gParser.Numero_negativoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(gParser.NUM_NEG)
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_comment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComentarioContext(CommentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.CommentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.ID)
            else:
                return self.getToken(gParser.ID, i)
        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NUM)
            else:
                return self.getToken(gParser.NUM, i)
        def NUM_NEG(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NUM_NEG)
            else:
                return self.getToken(gParser.NUM_NEG, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComentario" ):
                return visitor.visitComentario(self)
            else:
                return visitor.visitChildren(self)



    def comment(self):

        localctx = gParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comment)
        self._la = 0 # Token type
        try:
            localctx = gParser.ComentarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(gParser.T__25)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0):
                self.state = 124
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




