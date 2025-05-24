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
        4,1,22,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,3,0,16,8,0,1,0,3,0,19,8,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,41,
        8,2,11,2,12,2,42,1,2,3,2,46,8,2,1,2,1,2,1,2,1,2,5,2,52,8,2,10,2,
        12,2,55,9,2,1,3,1,3,3,3,59,8,3,1,4,1,4,4,4,63,8,4,11,4,12,4,64,1,
        5,1,5,1,6,1,6,1,6,0,1,4,7,0,2,4,6,8,10,12,0,3,1,0,19,21,1,0,6,17,
        2,0,7,7,18,18,73,0,23,1,0,0,0,2,32,1,0,0,0,4,45,1,0,0,0,6,58,1,0,
        0,0,8,60,1,0,0,0,10,66,1,0,0,0,12,68,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,19,3,8,4,0,18,17,1,0,0,0,
        18,19,1,0,0,0,19,20,1,0,0,0,20,22,5,1,0,0,21,15,1,0,0,0,22,25,1,
        0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,
        27,5,0,0,1,27,1,1,0,0,0,28,29,5,19,0,0,29,30,5,2,0,0,30,33,3,4,2,
        0,31,33,3,4,2,0,32,28,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,6,
        2,-1,0,35,36,5,3,0,0,36,37,3,4,2,0,37,38,5,4,0,0,38,46,1,0,0,0,39,
        41,3,6,3,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
        0,43,46,1,0,0,0,44,46,5,19,0,0,45,34,1,0,0,0,45,40,1,0,0,0,45,44,
        1,0,0,0,46,53,1,0,0,0,47,48,10,3,0,0,48,49,3,10,5,0,49,50,3,4,2,
        3,50,52,1,0,0,0,51,47,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,5,1,0,0,0,55,53,1,0,0,0,56,59,5,20,0,0,57,59,5,21,0,0,
        58,56,1,0,0,0,58,57,1,0,0,0,59,7,1,0,0,0,60,62,5,5,0,0,61,63,7,0,
        0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,9,
        1,0,0,0,66,67,7,1,0,0,67,11,1,0,0,0,68,69,7,2,0,0,69,13,1,0,0,0,
        9,15,18,23,32,42,45,53,58,64
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "'=:'", "'('", "')'", "'NB.'", 
                     "'+'", "'-'", "'*'", "'%'", "'^'", "'|'", "'='", "'<>'", 
                     "'<'", "'>'", "'<='", "'>='", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "NUM_NEG", "WS" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_operand = 3
    RULE_comment = 4
    RULE_operador_bin = 5
    RULE_operador_un = 6

    ruleNames =  [ "root", "statement", "expr", "operand", "comment", "operador_bin", 
                   "operador_un" ]

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
    ID=19
    NUM=20
    NUM_NEG=21
    WS=22

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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670058) != 0):
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670024) != 0):
                    self.state = 14
                    self.statement()


                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 17
                    self.comment()


                self.state = 20
                self.match(gParser.T__0)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = gParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(gParser.ID)
                self.state = 29
                self.match(gParser.T__1)
                self.state = 30
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = gParser.ExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
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


    class OperacionContext(ExprContext):

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
            if hasattr( visitor, "visitOperacion" ):
                return visitor.visitOperacion(self)
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = gParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 35
                self.match(gParser.T__2)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(gParser.T__3)
                pass
            elif token in [20, 21]:
                localctx = gParser.OperandoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 39
                        self.operand()

                    else:
                        raise NoViableAltException(self)
                    self.state = 42 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            elif token in [19]:
                localctx = gParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(gParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gParser.OperacionContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 47
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 48
                    self.operador_bin()
                    self.state = 49
                    self.expr(3) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 6, self.RULE_operand)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = gParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(gParser.NUM)
                pass
            elif token in [21]:
                localctx = gParser.Numero_negativoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
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
        self.enterRule(localctx, 8, self.RULE_comment)
        self._la = 0 # Token type
        try:
            localctx = gParser.ComentarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gParser.T__4)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 10, self.RULE_operador_bin)
        self._la = 0 # Token type
        try:
            localctx = gParser.Operador_binarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 262080) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_operador_un)
        self._la = 0 # Token type
        try:
            localctx = gParser.Operador_unarioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==7 or _la==18):
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
                return self.precpred(self._ctx, 3)
         




