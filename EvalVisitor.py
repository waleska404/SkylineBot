from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor



class TreeVisitor(SkylineVisitor):
    def __init__(self, dic):
        self.nivell = 0
        self.dicc = dic

    
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visit(ctx.expr(0))


    
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        nvar = int(len(ctx.variable()))
        nop = int(len(ctx.operation()))

        if nvar == 1:
            return self.visit(ctx.variable(0))
        elif nop == 1:
            return self.visit(ctx.operation(0))


    
    def visitVariable(self, ctx:SkylineParser.VariableContext):
        nsky = int(len(ctx.sky()))
        nop = int(len(ctx.operation()))
        var = str(ctx.VAR(0).getText())
        if nsky == 1:
            s = self.visit(ctx.sky(0))
            s.setID(var)
            dic[var] = s

        elif nop == 1:
            s = self.visit(ctx.operation(0))
            s.setID(var)
            dic[var] = s

    
    def visitSky(self, ctx:SkylineParser.SkyContext):
        #int(len(ctx.simple())) -> en teoria esto me devuelve el numero de simples que hay
        if ctx.simple(0):
            s1 = self.visit(ctx.simple(0))
            return s1
        elif ctx.compost(0):
            s1 = self.visit(ctx.compost(0))
            return s1
        else:
            s1 = self.visit(ctx.aleatori(0))
            return s1




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
        n = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        w = int(ctx.NUM(2).getText())
        xmin = int(ctx.NUM(3).getText())
        xmax = int(ctx.NUM(4).getText())
        s = Skyline.Skyline('null',0,0,0)
        s.random(n,h,w,xmin,xmax)
        return s


    
    def visitOperation(self, ctx:SkylineParser.OperationContext):
        nop = int(len(ctx.operation()))
        nmenys = int(len(ctx.MENYS()))
        nmult = int(len(ctx.MULT()))
        nmes = int(len(ctx.MES()))
        nvar = int(len(ctx.VAR()))
        nsky = int(len(ctx.sky()))
        nnum = int(len(ctx.NUM()))

        # brackets case
        if (nop == 1) and (nmult == 0) and (nmenys == 0) and (nmes == 0):
            return self.visit(ctx.operation(0))

        # mirror skyline case
        if (nop == 1) and (nmenys == 1) and (nnum == 0):
             s1 = self.visit(ctx.operation(0))
             return s1.mirrorSkyline()

        # intersection skyline case
        if (nop == 2) and (nmult == 1):
             s1 = self.visit(ctx.operation(0))
             s2 = self.visit(ctx.operation(1))
             return s1.intersecSkyline(s2)

        # replication skyline case
        if (nop == 1) and (nmult == 1) and (nnum == 1):
             s1 = self.visit(ctx.operation(0))
             n = self.visit(ctx.NUM(0).getText())
             return s1.replicateSkyline(n)

        # union skylines case
        if (nop == 2) and (nmes == 1):
             s1 = self.visit(ctx.operation(0))
             s2 = self.visit(ctx.operation(1))
             return s1.addSkyline(s2)

        # shift right skyline case
        if (nop == 1) and (nmes == 1) and (nnum == 1):
             s1 = self.visit(ctx.operation(0))
             n = self.visit(ctx.NUM(0).getText())
             return s1.shiftRight(n)

        # shift left skyline case
        if (nop == 1) and (nmenys == 1) and (nnum == 1):
             s1 = self.visit(ctx.operation(0))
             n = self.visit(ctx.NUM(0))
             return s1.shiftLeft(n)

        # VAR
        if (nvar == 1):
            #comprobar que esta en el diccionario
            var = str(ctx.VAR(0).getText())
            if var in self.dic 
                return dic[var]
            else:
                s = Skyline.Skyline(var, 0, 0, 0)
                dic[var] = s
                return s

        # sky
        if(nsky == 1):
            return self.visit(ctx.sky(0))