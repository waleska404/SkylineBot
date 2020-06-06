from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor



class TreeVisitor(SkylineVisitor):
    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#variable.
    def visitVariable(self, ctx:SkylineParser.VariableContext):
        return self.visitChildren(ctx)


    
    def visitSky(self, ctx:SkylineParser.SkyContext):
        if ctx.simple(0):
            s1 = ctx.simple(0)
            return s1
        elif ctx.compost(0):
            s1 = ctx.compost(0)
            return s1
        else:
            return ctx.aleatori(0)




    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        xmin = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        xmax = int(ctx.NUM(2).getText())
        n = 'null'
        s = Skyline.Skyline(n,xmin,h,xmax)
        return s


    
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        l = [self.visit(x) for x in ctx.simple()]
        s = Skyline.Skyline('null', 0,0,0)
        for elem in l:
            bl = elem.getBuildingsList()
            b = bl[0]
            s.addBuilding(b[0],b[1],b[2])
        return s



    def visitAleatori(self, ctx:SkylineParser.AleatoriContext):
        n = int(ctx.NUM(0))
        h = int(ctx.NUM(1))
        w = int(ctx.NUM(2))
        xmin = int(ctx.NUM(3))
        xmax = int(ctx.NUM(4))
        s = Skyline.Skyline('null',0,0,0)
        s.random(n,h,w,xmin,xmax)
        return s


    # Visit a parse tree produced by SkylineParser#operation.
    def visitOperation(self, ctx:SkylineParser.OperationContext):
        return self.visitChildren(ctx)