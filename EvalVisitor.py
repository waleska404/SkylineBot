from antlr4 import *
from skyline import Skyline
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor


class EvalVisitor(SkylineVisitor):
    def __init__(self, dic):
        self.nivell = 0
        self.dic = dic

    def visitRoot(self, ctx: SkylineParser.RootContext):
        n = ctx.getChildCount()
        l = next(ctx.getChildren()).getText()
        s = self.visit(next(ctx.getChildren()))
        return s

    def visitExpr(self, ctx: SkylineParser.ExprContext):
        nvar = (ctx.variable())
        nop = (ctx.operation())

        if (nvar):
            return self.visit(ctx.variable())
        elif (nop):
            return self.visit(ctx.operation())

    def visitVariable(self, ctx: SkylineParser.VariableContext):
        nsky = (ctx.sky())
        nop = (ctx.operation())
        var = str(ctx.VAR().getText())
        if (nsky):
            s = self.visit(ctx.sky())
            s.setID(var)
            self.dic[var] = s
            return s

        elif (nop):
            s = self.visit(ctx.operation())
            s.setID(var)
            self.dic[var] = s
            return s

    def visitSky(self, ctx: SkylineParser.SkyContext):
        if ctx.simple():
            s1 = self.visit(ctx.simple())
            return s1
        elif ctx.compost():
            s1 = self.visit(ctx.compost())
            return s1
        else:
            s1 = self.visit(ctx.aleatori())
            return s1

    def visitSimple(self, ctx: SkylineParser.SimpleContext):
        xmin = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        xmax = int(ctx.NUM(2).getText())
        n = 'null'
        s = Skyline(n, xmin, h, xmax)
        l = s.getBuildingsList()
        return s

    def visitCompost(self, ctx: SkylineParser.CompostContext):
        l = [self.visit(x) for x in ctx.simple()]
        s = l[0]
        l.pop(0)
        for elem in l:
            bl = elem.getBuildingsList()
            b = bl[0]
            s.addBuilding(b[0], b[1], b[2])

        lll = s.getBuildingsList()
        return s

    def visitAleatori(self, ctx: SkylineParser.AleatoriContext):
        n = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        w = int(ctx.NUM(2).getText())
        xmin = int(ctx.NUM(3).getText())
        xmax = int(ctx.NUM(4).getText())
        s = Skyline('null', 0, 0, 0)
        r = s.randomFunc(n, h, w, xmin, xmax)
        return r

    def visitOperation(self, ctx: SkylineParser.OperationContext):
        nop = (ctx.operation())
        nmenys = (ctx.MENYS())
        nmult = (ctx.MULT())
        nmes = (ctx.MES())
        nvar = (ctx.VAR())
        nsky = (ctx.sky())
        nnum = (ctx.NUM())

        # brackets case
        if (nop) and (not nmult) and (not nmenys) and (not nmes):
            s = self.visit(ctx.operation(0))
            return s

        # mirror skyline case
        if (nop) and (nmenys) and (not nnum):
            s1 = self.visit(ctx.operation(0))
            r = s1.mirrorSkyline()
            return r

        # intersection skyline case
        if (nop) and (nmult) and (not nnum):
            s1 = self.visit(ctx.operation(0))
            s2 = self.visit(ctx.operation(1))
            r = s1.intersecSkyline(s2)
            lr = r.getBuildingsList()
            return r

        # replication skyline case
        if (nop) and (nmult) and (nnum):
            s1 = self.visit(ctx.operation(0))
            l = s1.getBuildingsList()

            n = int(ctx.NUM().getText())
            r = s1.replicateSkyline(n)
            return r

        # union skylines case
        if (nop) and (nmes) and (not nnum):
            s1 = self.visit(ctx.operation(0))
            l1 = s1.getBuildingsList()
            s2 = self.visit(ctx.operation(1))
            l2 = s2.getBuildingsList()
            ss1 = s1.addSkyline(s2)
            l3 = ss1.getBuildingsList()
            return ss1

        # shift right skyline case
        if (nop) and (nmes) and (nnum):
            s1 = self.visit(ctx.operation(0))
            n = int(ctx.NUM().getText())
            l = s1.getBuildingsList()
            r = s1.shiftRight(n)
            return r

        # shift left skyline case
        if (nop) and (nmenys) and (nnum):
            s1 = self.visit(ctx.operation(0))
            n = int(ctx.NUM().getText())
            r = s1.shiftLeft(n)
            return r

        # VAR
        if (nvar):
            var = str(ctx.VAR().getText())
            if (var in self.dic):
                dic2 = (self.dic).copy()
                d2 = dic2[var]
                return d2
            else:
                s = Skyline('NOEXISTE404', 0, 0, 0)
                return s

        # sky
        if(nsky):
            return self.visit(ctx.sky())
