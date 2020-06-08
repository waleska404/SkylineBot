# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\n\62\n\n\r\n\16\n")
        buf.write("\63\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16=\n\16\r\16\16")
        buf.write("\16>\3\16\3\16\3\17\6\17D\n\17\r\17\16\17E\3\17\7\17I")
        buf.write("\n\17\f\17\16\17L\13\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\6\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\4\2C\\c|\5\2\62;C\\c|\2P\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\3\37\3\2\2\2\5\"\3\2\2\2\7$\3\2\2\2\t&\3")
        buf.write("\2\2\2\13(\3\2\2\2\r*\3\2\2\2\17,\3\2\2\2\21.\3\2\2\2")
        buf.write("\23\61\3\2\2\2\25\65\3\2\2\2\27\67\3\2\2\2\319\3\2\2\2")
        buf.write("\33<\3\2\2\2\35C\3\2\2\2\37 \7<\2\2 !\7?\2\2!\4\3\2\2")
        buf.write("\2\"#\7*\2\2#\6\3\2\2\2$%\7.\2\2%\b\3\2\2\2&\'\7+\2\2")
        buf.write("\'\n\3\2\2\2()\7]\2\2)\f\3\2\2\2*+\7_\2\2+\16\3\2\2\2")
        buf.write(",-\7}\2\2-\20\3\2\2\2./\7\177\2\2/\22\3\2\2\2\60\62\t")
        buf.write("\2\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\24\3\2\2\2\65\66\7-\2\2\66\26\3\2\2\2\678")
        buf.write("\7,\2\28\30\3\2\2\29:\7/\2\2:\32\3\2\2\2;=\t\3\2\2<;\3")
        buf.write("\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\b\16")
        buf.write("\2\2A\34\3\2\2\2BD\t\4\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2")
        buf.write("\2EF\3\2\2\2FJ\3\2\2\2GI\t\5\2\2HG\3\2\2\2IL\3\2\2\2J")
        buf.write("H\3\2\2\2JK\3\2\2\2K\36\3\2\2\2LJ\3\2\2\2\t\2\63>CEHJ")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NUM = 9
    MES = 10
    MULT = 11
    MENYS = 12
    WS = 13
    VAR = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "','", "')'", "'['", "']'", "'{'", "'}'", "'+'", 
            "'*'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "MULT", "MENYS", "WS", "VAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "NUM", "MES", "MULT", "MENYS", "WS", "VAR" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


