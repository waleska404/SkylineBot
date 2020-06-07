from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

from skyline import Skyline

class EvalVisitor(SkylineVisitor):
    def __init__(self, dic):
        self.nivell = 0
        self.dic = dic

    
    def visitRoot(self, ctx:SkylineParser.RootContext):
        print('visitROot:')
        n = ctx.getChildCount()
        l = next(ctx.getChildren()).getText()
        print(l)
        print(n)
        s = self.visit(next(ctx.getChildren()))
        print('get children')
        return s
        print ('return')


    
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        print('visitExpr:')
        nvar = (ctx.variable())
        #nvar = int(len(ctx.variable(0)))
        nop = (ctx.operation())
        print('nvar y nop:')
        print(nvar)
        print(nop)
        print('nvar y nop')

        if (nvar):
            return self.visit(ctx.variable())
        elif (nop):
            print('entro en elif de nop')
            return self.visit(ctx.operation())


    
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
        print('entro en visitSky:')
        #int(len(ctx.simple())) -> en teoria esto me devuelve el numero de simples que hay
        if ctx.simple():
            s1 = self.visit(ctx.simple())
            return s1
        elif ctx.compost():
            s1 = self.visit(ctx.compost())
            return s1
        else:
            s1 = self.visit(ctx.aleatori())
            return s1




    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        print('entro en simple')
        xmin = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        xmax = int(ctx.NUM(2).getText())
        n = 'null'
        s = Skyline(n,xmin,h,xmax)
        l = s.getBuildingsList()
        print('skyline simple:')
        print(l)
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
        print('visito operation')
        nop = (ctx.operation())
        nmenys = (ctx.MENYS())
        nmult = (ctx.MULT())
        nmes = (ctx.MES())
        nvar = (ctx.VAR())
        nsky = (ctx.sky())
        nnum = (ctx.NUM())

        # brackets case
        if (nop) and (not nmult) and (not nmenys) and (not nmes):
            print('entro en if brackets')
            return self.visit(ctx.operation())

        # mirror skyline case
        if (nop) and (nmenys) and (not nnum):
             print('entro en if mirror')
             s1 = self.visit(ctx.operation(0))
             return s1.mirrorSkyline()

        # intersection skyline case
        if (nop) and (nmult):
             print('entro en if intersection')
             s1 = self.visit(ctx.operation(0))
             s2 = self.visit(ctx.operation(1))
             return s1.intersecSkyline(s2)

        # replication skyline case
        if (nop) and (nmult) and (nnum):
             print('entro en if replication')
             s1 = self.visit(ctx.operation(0))
             n = self.visit(ctx.NUM(0).getText())
             return s1.replicateSkyline(n)

        # union skylines case
        if (nop) and (nmes):
             print('entro en if union')
             s1 = self.visit(ctx.operation(0))
             l1 = s1.getBuildingsList()
             print('l1:')
             print(l1)
             s2 = self.visit(ctx.operation(1))
             l2 = s2.getBuildingsList()
             print('l2:')
             print(l2)
             s1.addSkyline(s2)
             l3 = s1.getBuildingsList()
             print('buildinfs s3')
             print(l3)
             return s1

        # shift right skyline case
        if (nop) and (nmes) and (nnum):
             print('entro en if shift right')
             s1 = self.visit(ctx.operation(0))
             n = self.visit(ctx.NUM(0).getText())
             return s1.shiftRight(n)

        # shift left skyline case
        if (nop) and (nmenys) and (nnum):
             print('entro en if shift left')
             s1 = self.visit(ctx.operation(0))
             n = self.visit(ctx.NUM(0))
             return s1.shiftLeft(n)

        # VAR
        if (nvar):
            print('entro en if n var')
            #comprobar que esta en el diccionario
            var = str(ctx.VAR(0).getText())
            if (var in self.dic):
                return dic[var]
            else:
                s = Skyline.Skyline(var, 0, 0, 0)
                dic[var] = s
                return s

        # sky
        if(nsky):
            print('entro en el if de sky')
            return self.visit(ctx.sky())



