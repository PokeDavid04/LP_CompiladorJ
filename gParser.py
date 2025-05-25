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
        4,1,29,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,3,0,23,8,0,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,52,8,2,11,2,12,2,53,1,2,
        3,2,57,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,68,8,2,10,2,12,
        2,71,9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,3,7,83,8,7,1,8,
        1,8,5,8,87,8,8,10,8,12,8,90,9,8,1,8,0,1,4,9,0,2,4,6,8,10,12,14,16,
        0,4,1,0,5,19,2,0,18,18,20,21,1,0,23,24,1,0,26,28,95,0,27,1,0,0,0,
        2,36,1,0,0,0,4,56,1,0,0,0,6,72,1,0,0,0,8,74,1,0,0,0,10,76,1,0,0,
        0,12,78,1,0,0,0,14,82,1,0,0,0,16,84,1,0,0,0,18,20,3,2,1,0,19,18,
        1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,23,3,16,8,0,22,21,1,0,0,0,
        22,23,1,0,0,0,23,24,1,0,0,0,24,26,5,1,0,0,25,19,1,0,0,0,26,29,1,
        0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,
        31,5,0,0,1,31,1,1,0,0,0,32,33,5,26,0,0,33,34,5,2,0,0,34,37,3,4,2,
        0,35,37,3,4,2,0,36,32,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,6,
        2,-1,0,39,40,5,3,0,0,40,41,3,4,2,0,41,42,5,4,0,0,42,57,1,0,0,0,43,
        44,3,8,4,0,44,45,3,4,2,5,45,57,1,0,0,0,46,47,3,6,3,0,47,48,3,12,
        6,0,48,49,3,4,2,3,49,57,1,0,0,0,50,52,3,14,7,0,51,50,1,0,0,0,52,
        53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,57,1,0,0,0,55,57,5,26,
        0,0,56,38,1,0,0,0,56,43,1,0,0,0,56,46,1,0,0,0,56,51,1,0,0,0,56,55,
        1,0,0,0,57,69,1,0,0,0,58,59,10,6,0,0,59,60,3,6,3,0,60,61,3,4,2,6,
        61,68,1,0,0,0,62,63,10,4,0,0,63,64,3,6,3,0,64,65,3,10,5,0,65,66,
        3,4,2,4,66,68,1,0,0,0,67,58,1,0,0,0,67,62,1,0,0,0,68,71,1,0,0,0,
        69,67,1,0,0,0,69,70,1,0,0,0,70,5,1,0,0,0,71,69,1,0,0,0,72,73,7,0,
        0,0,73,7,1,0,0,0,74,75,7,1,0,0,75,9,1,0,0,0,76,77,5,22,0,0,77,11,
        1,0,0,0,78,79,7,2,0,0,79,13,1,0,0,0,80,83,5,27,0,0,81,83,5,28,0,
        0,82,80,1,0,0,0,82,81,1,0,0,0,83,15,1,0,0,0,84,88,5,25,0,0,85,87,
        7,3,0,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,17,1,0,0,0,90,88,1,0,0,0,10,19,22,27,36,53,56,67,69,82,88
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "'=:'", "'('", "')'", "'+'", 
                     "'-'", "'*'", "'%'", "'^'", "'|'", "'='", "'<>'", "'<'", 
                     "'>'", "'<='", "'>='", "','", "'#'", "'{'", "']'", 
                     "'i.'", "'~'", "':'", "'/'", "'NB.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUM", "NUM_NEG", 
                      "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_operador_bin = 3
    RULE_operador_un = 4
    RULE_operador_bin_comb = 5
    RULE_operador_un_comb = 6
    RULE_operand = 7
    RULE_comment = 8

    ruleNames =  [ "root", "statement", "expr", "operador_bin", "operador_un", 
                   "operador_bin_comb", "operador_un_comb", "operand", "comment" ]

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
    ID=26
    NUM=27
    NUM_NEG=28
    WS=29

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 507510762) != 0):
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 473956328) != 0):
                    self.state = 18
                    self.statement()


                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 21
                    self.comment()


                self.state = 24
                self.match(gParser.T__0)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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



    def statement(self):

        localctx = gParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = gParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(gParser.ID)
                self.state = 33
                self.match(gParser.T__1)
                self.state = 34
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = gParser.ExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.expr(0)
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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = gParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 39
                self.match(gParser.T__2)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(gParser.T__3)
                pass

            elif la_ == 2:
                localctx = gParser.Operacion_unariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.operador_un()
                self.state = 44
                self.expr(5)
                pass

            elif la_ == 3:
                localctx = gParser.Operacion_unaria_combinadaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.operador_bin()
                self.state = 47
                self.operador_un_comb()
                self.state = 48
                self.expr(3)
                pass

            elif la_ == 4:
                localctx = gParser.OperandoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 50
                        self.operand()

                    else:
                        raise NoViableAltException(self)
                    self.state = 53 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 5:
                localctx = gParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(gParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = gParser.Operacion_binariaContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 59
                        self.operador_bin()
                        self.state = 60
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = gParser.Operacion_binaria_combinadaContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 63
                        self.operador_bin()
                        self.state = 64
                        self.operador_bin_comb()
                        self.state = 65
                        self.expr(4)
                        pass

             
                self.state = 71
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
            self.state = 72
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
            self.state = 74
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
            self.state = 76
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
            self.state = 78
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
        self.enterRule(localctx, 14, self.RULE_operand)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = gParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(gParser.NUM)
                pass
            elif token in [28]:
                localctx = gParser.Numero_negativoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 81
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
        self.enterRule(localctx, 16, self.RULE_comment)
        self._la = 0 # Token type
        try:
            localctx = gParser.ComentarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(gParser.T__24)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 85
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 90
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




