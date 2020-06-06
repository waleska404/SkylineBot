# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#variable.
    def visitVariable(self, ctx:SkylineParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx:SkylineParser.SkyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#simple.
    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#aleatori.
    def visitAleatori(self, ctx:SkylineParser.AleatoriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#operation.
    def visitOperation(self, ctx:SkylineParser.OperationContext):
        return self.visitChildren(ctx)



del SkylineParser