# Generated from Skyline.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\5\3\30\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\5\5%\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\63\n\7\f\7")
        buf.write("\16\7\66\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\tO\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\7\t`\n\t\f\t\16\tc\13\t\3\t\2\3\20\n\2")
        buf.write("\4\6\b\n\f\16\20\2\2\2i\2\22\3\2\2\2\4\27\3\2\2\2\6\37")
        buf.write("\3\2\2\2\b$\3\2\2\2\n&\3\2\2\2\f.\3\2\2\2\169\3\2\2\2")
        buf.write("\20N\3\2\2\2\22\23\5\4\3\2\23\24\7\2\2\3\24\3\3\2\2\2")
        buf.write("\25\30\5\6\4\2\26\30\5\20\t\2\27\25\3\2\2\2\27\26\3\2")
        buf.write("\2\2\30\5\3\2\2\2\31\32\7\20\2\2\32\33\7\3\2\2\33 \5\b")
        buf.write("\5\2\34\35\7\20\2\2\35\36\7\3\2\2\36 \5\20\t\2\37\31\3")
        buf.write("\2\2\2\37\34\3\2\2\2 \7\3\2\2\2!%\5\n\6\2\"%\5\f\7\2#")
        buf.write("%\5\16\b\2$!\3\2\2\2$\"\3\2\2\2$#\3\2\2\2%\t\3\2\2\2&")
        buf.write("\'\7\4\2\2\'(\7\13\2\2()\7\5\2\2)*\7\13\2\2*+\7\5\2\2")
        buf.write("+,\7\13\2\2,-\7\6\2\2-\13\3\2\2\2./\7\7\2\2/\64\5\n\6")
        buf.write("\2\60\61\7\5\2\2\61\63\5\n\6\2\62\60\3\2\2\2\63\66\3\2")
        buf.write("\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66\64\3")
        buf.write("\2\2\2\678\7\b\2\28\r\3\2\2\29:\7\t\2\2:;\7\13\2\2;<\7")
        buf.write("\5\2\2<=\7\13\2\2=>\7\5\2\2>?\7\13\2\2?@\7\5\2\2@A\7\13")
        buf.write("\2\2AB\7\5\2\2BC\7\13\2\2CD\7\n\2\2D\17\3\2\2\2EF\b\t")
        buf.write("\1\2FG\7\4\2\2GH\5\20\t\2HI\7\6\2\2IO\3\2\2\2JK\7\16\2")
        buf.write("\2KO\5\20\t\nLO\7\20\2\2MO\5\b\5\2NE\3\2\2\2NJ\3\2\2\2")
        buf.write("NL\3\2\2\2NM\3\2\2\2Oa\3\2\2\2PQ\f\t\2\2QR\7\r\2\2R`\5")
        buf.write("\20\t\nST\f\7\2\2TU\7\f\2\2U`\5\20\t\bVW\f\b\2\2WX\7\r")
        buf.write("\2\2X`\7\13\2\2YZ\f\6\2\2Z[\7\f\2\2[`\7\13\2\2\\]\f\5")
        buf.write("\2\2]^\7\16\2\2^`\7\13\2\2_P\3\2\2\2_S\3\2\2\2_V\3\2\2")
        buf.write("\2_Y\3\2\2\2_\\\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2")
        buf.write("b\21\3\2\2\2ca\3\2\2\2\t\27\37$\64N_a")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "','", "')'", "'['", "']'", 
                     "'{'", "'}'", "<INVALID>", "'+'", "'*'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "MES", "MULT", "MENYS", "WS", 
                      "VAR" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_variable = 2
    RULE_sky = 3
    RULE_simple = 4
    RULE_compost = 5
    RULE_aleatori = 6
    RULE_operation = 7

    ruleNames =  [ "root", "expr", "variable", "sky", "simple", "compost", 
                   "aleatori", "operation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUM=9
    MES=10
    MULT=11
    MENYS=12
    WS=13
    VAR=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.expr()
            self.state = 17
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(SkylineParser.VariableContext,0)


        def operation(self):
            return self.getTypedRuleContext(SkylineParser.OperationContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_expr




    def expr(self):

        localctx = SkylineParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.operation(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def sky(self):
            return self.getTypedRuleContext(SkylineParser.SkyContext,0)


        def operation(self):
            return self.getTypedRuleContext(SkylineParser.OperationContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_variable




    def variable(self):

        localctx = SkylineParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(SkylineParser.VAR)
                self.state = 24
                self.match(SkylineParser.T__0)
                self.state = 25
                self.sky()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(SkylineParser.VAR)
                self.state = 27
                self.match(SkylineParser.T__0)
                self.state = 28
                self.operation(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SkyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self):
            return self.getTypedRuleContext(SkylineParser.SimpleContext,0)


        def compost(self):
            return self.getTypedRuleContext(SkylineParser.CompostContext,0)


        def aleatori(self):
            return self.getTypedRuleContext(SkylineParser.AleatoriContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_sky




    def sky(self):

        localctx = SkylineParser.SkyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sky)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.simple()
                pass
            elif token in [SkylineParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.compost()
                pass
            elif token in [SkylineParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.aleatori()
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

    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_simple




    def simple(self):

        localctx = SkylineParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SkylineParser.T__1)
            self.state = 37
            self.match(SkylineParser.NUM)
            self.state = 38
            self.match(SkylineParser.T__2)
            self.state = 39
            self.match(SkylineParser.NUM)
            self.state = 40
            self.match(SkylineParser.T__2)
            self.state = 41
            self.match(SkylineParser.NUM)
            self.state = 42
            self.match(SkylineParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SimpleContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SimpleContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_compost




    def compost(self):

        localctx = SkylineParser.CompostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SkylineParser.T__4)
            self.state = 45
            self.simple()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__2:
                self.state = 46
                self.match(SkylineParser.T__2)
                self.state = 47
                self.simple()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(SkylineParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AleatoriContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_aleatori




    def aleatori(self):

        localctx = SkylineParser.AleatoriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SkylineParser.T__6)
            self.state = 56
            self.match(SkylineParser.NUM)
            self.state = 57
            self.match(SkylineParser.T__2)
            self.state = 58
            self.match(SkylineParser.NUM)
            self.state = 59
            self.match(SkylineParser.T__2)
            self.state = 60
            self.match(SkylineParser.NUM)
            self.state = 61
            self.match(SkylineParser.T__2)
            self.state = 62
            self.match(SkylineParser.NUM)
            self.state = 63
            self.match(SkylineParser.T__2)
            self.state = 64
            self.match(SkylineParser.NUM)
            self.state = 65
            self.match(SkylineParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.OperationContext)
            else:
                return self.getTypedRuleContext(SkylineParser.OperationContext,i)


        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def sky(self):
            return self.getTypedRuleContext(SkylineParser.SkyContext,0)


        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_operation



    def operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.OperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_operation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 68
                self.match(SkylineParser.T__1)
                self.state = 69
                self.operation(0)
                self.state = 70
                self.match(SkylineParser.T__3)
                pass

            elif la_ == 2:
                self.state = 72
                self.match(SkylineParser.MENYS)
                self.state = 73
                self.operation(8)
                pass

            elif la_ == 3:
                self.state = 74
                self.match(SkylineParser.VAR)
                pass

            elif la_ == 4:
                self.state = 75
                self.sky()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 78
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 79
                        self.match(SkylineParser.MULT)
                        self.state = 80
                        self.operation(8)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 81
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 82
                        self.match(SkylineParser.MES)
                        self.state = 83
                        self.operation(6)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 84
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 85
                        self.match(SkylineParser.MULT)
                        self.state = 86
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 87
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 88
                        self.match(SkylineParser.MES)
                        self.state = 89
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.OperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 90
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 91
                        self.match(SkylineParser.MENYS)
                        self.state = 92
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[7] = self.operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operation_sempred(self, localctx:OperationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




