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
        print('entro en visitExpr:')
        nvar = (ctx.variable())
        #nvar = int(len(ctx.variable(0)))
        nop = (ctx.operation())

        if (nvar):
            ('entro en el id de nop')
            return self.visit(ctx.variable())
        elif (nop):
            print('entro en elif de nop')
            return self.visit(ctx.operation())


    
    def visitVariable(self, ctx:SkylineParser.VariableContext):
        print('entro en visit variable')
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
        print('visitCompost')
        l = [self.visit(x) for x in ctx.simple()]
        s = l[0]
        print('s:')
        print(s)
        print('l:')
        l.pop(0)
        print(l)
        for elem in l:
            bl = elem.getBuildingsList()
            print('bl dentro del for')
            print(bl)
            b = bl[0]
            print('b dentro del fot')
            print(b[0])
            s.addBuilding(b[0],b[1],b[2])

        print("voy a retornar s")
        lll = s.getBuildingsList()
        print(lll)
        return s



    def visitAleatori(self, ctx:SkylineParser.AleatoriContext):
        print('entro en visit aleatori')
        n = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        w = int(ctx.NUM(2).getText())
        xmin = int(ctx.NUM(3).getText())
        xmax = int(ctx.NUM(4).getText())
        s = Skyline('null',0,0,0)
        r = s.randomFunc(n,h,w,xmin,xmax)
        return r


    
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
            s = self.visit(ctx.operation(0))
            return s

        # mirror skyline case
        if (nop) and (nmenys) and (not nnum):
             print('entro en if mirror')
             s1 = self.visit(ctx.operation(0))
             r = s1.mirrorSkyline()
             return r

        # intersection skyline case
        if (nop) and (nmult) and (not nnum):
             print('entro en if intersection')
             s1 = self.visit(ctx.operation(0))
             s2 = self.visit(ctx.operation(1))
             r = s1.intersecSkyline(s2)
             print('PRINT DE R')
             lr = r.getBuildingsList()
             print(lr)
             return r

        # replication skyline case
        if (nop) and (nmult) and (nnum):
             print('entro en if replication')
             s1 = self.visit(ctx.operation(0))
             l = s1.getBuildingsList()
             print(l)

             n = int(ctx.NUM().getText())
             print(n)
             r = s1.replicateSkyline(n)
             return r

        # union skylines case
        if (nop) and (nmes) and (not nnum):
             print('entro en if union')

             s1 = self.visit(ctx.operation(0))
             l1 = s1.getBuildingsList()
             print('l1:')
             print(l1)
             s2 = self.visit(ctx.operation(1))
             l2 = s2.getBuildingsList()

             print('l2:')
             print(l2)
             
             ss1 = s1.addSkyline(s2)

             l3 = ss1.getBuildingsList()
             print('buildinfs s3')
             print(l3)
             #id = ss1.getID()
             #ss = self.dic[id]
             #ll = ss.getBuildingsList()
             #print('lis Buid DICCIONARIO s1')
             #print(ll)
             return ss1

        # shift right skyline case
        if (nop) and (nmes) and (nnum):
             print('entro en if shift right')
             s1 = self.visit(ctx.operation(0))
             n = int(ctx.NUM().getText())
             l = s1.getBuildingsList()
             print('bl en shitf right de eval')
             print(l)
             r = s1.shiftRight(n)
             return r

        # shift left skyline case
        if (nop) and (nmenys) and (nnum):
             print('entro en if shift left')
             s1 = self.visit(ctx.operation(0))
             n = int(ctx.NUM().getText())
             r = s1.shiftLeft(n)
             return r

        # VAR
        if (nvar):
            print('entro en if n var')
            #comprobar que esta en el diccionario
            var = str(ctx.VAR().getText())
            if (var in self.dic):
                dic2 = (self.dic).copy()
                #dic2 = copy.deepcopy(dic22)
                d2 = dic2[var] #saco el skyline con id Var
                print('asig heach')
                l = d2.getBuildingsList() 
                print(l)
                print('VOY A MODIFICAR')
                dic2[var] = Skyline('oli',0,0,0)
                id = (self.dic[var]).getID()
                id2 = (dic2[var]).getID()
                print(id)
                print(id2)
                return d2 #le devuelvo el skyline con id var
            else:
                s = Skyline('NOEXISTE404', 0, 0, 0)
                #TODO: NO SE COMO GESTIONARLO
                #QUIZA DECIRLE QUE ESTA UTILIZANDO UNA VARIBALE SIN VALOR
                return s

        # sky
        if(nsky):
            print('entro en el if de sky')
            return self.visit(ctx.sky())



