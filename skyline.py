import matplotlib.pyplot as plt
import datetime
import random


class Skyline:

    def __init__(self, id, xmin, height, xmax):
        b1 = (xmin, height, xmax)
        bl = [b1]
        self.id = id
        self.bl = bl  # bl = buildings list


    # ##########SETTERS########### #

    def setID(self, id2):
        self.id = id2

    # ##########GETTERS########### #

    # returns the skyline's buildings list
    def getBuildingsList(self):
        return self.bl

    # returns the skyline's id
    def getID(self):
        return self.id

    # retunrs the slyline's area
    def getArea(self):
        self.noOverlapping()
        suma = 0
        for k in self.bl:
            s = self.buildingArea(k)
            suma += s
        return suma

    # returns the skyline's height
    def getHeight(self):
        maxi = 0
        for k in self.bl:
            if k[1] > maxi:
                maxi = k[1]
        return maxi


    # ########OPERATIONS########## #

    # add a building to the current skyline
    def addBuilding(self, xmin, height, xmax):
        self.bl += [(xmin, height, xmax)]
    

    # returns the union of two skylines
    def addSkyline(self, skyobj):
        l1 = (self.bl).copy()
        l2 = skyobj.getBuildingsList()
        l3 = l1+l2
        elem = l3[0]
        l3.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in l3:
            s.addBuilding(k[0],k[1],k[2])
        s.noOverlapping()
        return s


    # return the intersection between skyobj and current skyline
    def intersecSkyline(self, skyobj):
        bl1 = (self.bl).copy()
        bl2 = skyobj.getBuildingsList()
 
        lim11 = bl1[0][0]
        lim12 = bl1[-1][2]
      
        lim21 = bl2[0][0]
        lim22 = bl2[-1][2]

        limLeft = max(lim11, lim21)
        limRight = min(lim12, lim22)
    
        edges1 = []
        edges2 = []
  
        edges1.extend([building[0],building[2]] for building in bl1)
      
        edges1 = (sum(edges1,[])) 
        

        edges2.extend([building[0],building[2]] for building in bl2)
        edges2 = (sum(edges2,[])) 
        

        edaux = edges1 + edges2
        edaux = sorted(edaux)
 
        
        edges = [edg for edg in edaux if(edg >= limLeft and edg <= limRight)]
        edges = set(edges)
        edges = list(edges)
      
        current = 0
        points = []
      
        buildings1bis = [b for b in bl1 if((b[0] > limLeft and b[0] < limRight) or (b[2] > limLeft and b[2] < limRight) or (b[0] <= limLeft and b[2] >= limRight))]
        buildings2bis = [b for b in bl2 if((b[0] > limLeft and b[0] < limRight) or (b[2] > limLeft and b[2] < limRight) or (b[0] <= limLeft and b[2] >= limRight))]
        buildings = buildings1bis + buildings2bis
        
        for i in edges:
            active = []
            active.extend(building for building in buildings if ((building[0] <= i and building[2] > i) or (building[0] < i and building[2] > i)))
            
            if len(active) <= 1: 
                current = 0
                points.append((i,0))
                continue
            min_h = min(building[1] for building in active)
            min_ed = i
            
            if min_h != current:
                current = min_h
                points.append((i,min_h))

        last = edges[-1]
        points.append((last, 0))
        l = []
        for index, item in enumerate(points):
            if index < len(points)-1:
                a = item[0]
                b = item[1]
                elem = points[index+1]
                c = elem[0]
                if b != 0:
                    l.append((a,b,c))

        elem = l[0]
        l.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in l:
            s.addBuilding(k[0],k[1],k[2])
        
        lr = s.getBuildingsList()
        return s  


    # returns the refelction of the current skyline
    def mirrorSkyline(self):
        
        l = (self.bl).copy()
        l2 = []

        w = 0
        minx = l[0][0]
        maxx = l[0][2]
        
        for elem in l:
            if elem[0] < minx:
                minx = elem[0]
            if elem[2] > maxx:
                maxx = elem[2]

        center = (minx+maxx)/2
        
        for elem in l:
            #edificio a la izquierda del centro
            if (elem[0] < center) and (elem[2] <= center):
                dist0 = center - elem[0]
                pos2 = center + dist0
                dist2 = center - elem[2]
                pos0 = center + dist2
                pos1 = elem[1]
                l2.append((pos0,pos1,pos2))

            #edificio a la derecha del centro
            if (elem[0] >= center) and (elem[2] > center):
                dist0 = elem[0] - center
                pos2 = center - dist0
                dist2 = elem[2] - center
                pos0 = center - dist2
                pos1 = elem[1]
                l2.append((pos0,pos1,pos2))

            #edificio a la derecha e izquierda del centro
            if (elem[0] < center) and (elem[2] > center):
                dist0 = center - elem[0]
                pos2 = center + dist0
                dist2 = elem[2] - center
                pos0 = center - dist2
                pos1 = elem[1]
                l2.append((pos0,pos1,pos2))

        elem = l2[0]
        l2.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in l2:
            s.addBuilding(k[0],k[1],k[2])
        
        lr = s.getBuildingsList()
        return s  
       




    # replicate the skyline n times
    def replicateSkyline(self, n):
        l = (self.bl).copy()
        lr = (self.bl).copy()
        w = 0
        minx = l[0][0]
        maxx = l[0][2]
        
        for elem in l:
            if elem[0] < minx:
                minx = elem[0]
            if elem[2] > maxx:
                maxx = elem[2]

        w = maxx - minx

        ampOrig = w

        for k in range(n-1):
            laux = []
            for j in l:
                j = list(j)
                j[0] += w
                j[2] += w
                j = tuple(j)
                laux.append(j)
            w = w + ampOrig
            lr += laux

        elem = lr[0]
        lr.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in lr:
            s.addBuilding(k[0],k[1],k[2])
        
        lr2 = s.getBuildingsList()
        return s  

    # shift skyline n positions to the right
    def shiftRight(self, n):
        l = []
        aux = (self.bl).copy()
        for k in aux:
            k = list(k)
            k[0] += n
            k[2] += n
            k = tuple(k)
            l.append(k)
        
        elem = l[0]
        l.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in l:
            s.addBuilding(k[0],k[1],k[2])
        
        lr2 = s.getBuildingsList()
        return s  


    # shift skyline n positions to the left
    def shiftLeft(self, n):
        l = []
        aux = (self.bl).copy()
        for k in aux:
            k = list(k)
            k[0] -= n
            k[2] -= n
            k = tuple(k)
            l.append(k)
        elem = l[0]
        l.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in l:
            s.addBuilding(k[0],k[1],k[2])
        
        lr2 = s.getBuildingsList()
        return s
    
    # returns the especified random skyline
    def randomFunc(self,n, h, w, xmin, xmax):
        a = random.randint(xmin, xmax-1)
        b = random.randint(0, h)
        c = random.randint(a+1, xmax)
        s = Skyline('null',a,b,c)
        it = 0
        nn = n-1
        while it < n-1:
            a2 = random.randint(xmin, xmax-1)
            b2 = random.randint(0, h)
            c2 = random.randint(a2+1, xmax)
            s.addBuilding(a2,b2,c2)
            it += 1
        l = s.getBuildingsList()
        s.noOverlapping()
        return s


    # ########PROCESSING########## #
    
    # creates the skyline's plot
    def plotProcessing(self):
        if self.id == 'null':
            id = str(datetime.datetime.now())
            id = id.replace(" ","")
            id = id.replace(".","")
            id = id.replace(":","")
            id = id.replace("-","")
            self.id = id
        xl = []
        widthl = []
        heightl = []
        for k in self.bl:
            w = k[2] - k[0]
            xl += [k[0]]
            widthl += [w]
            heightl += [k[1]]
        plt.bar(xl, heightl, widthl, 0, align='edge')
        plt.savefig(str(self.id))
        plt.clf()


    # ###########UTILS############ #
    def graterThan(self,a,b): # a > b
        if (a[0] > b[0]):
            return True
        else:
            return False

    def equals(self,a,b): # a == b
        if (a[0] == b[0]):
            return True
        else:
            return False

    def lowerEq(self,a,b): # a <= b
        if(a[0] <= b[0]):
           return True
        else:
            return False

    def graterEq(self,a,b): # a >= b
        if(a[0] >= b[0]):
           return True
        else:
            return False
    
    def buildingArea(self, b):
        y = b[1]
        z = b[2]
        x = b[0]
        a = (y+1)*(z-x)
        return a
    
    def noOverlapping(self):
        buildings = self.bl
        edges = []
        edges.extend([building[0],building[2]] for building in buildings)
        edges = sorted(sum(edges,[])) 
 
        current = 0
        points = []
  
        for i in edges:
            active = []
            active.extend(building for building in buildings if (building[0] <= i and building[2] > i)) 
            if not active: 
                current = 0
                points.append((i,0))
                continue
            max_h = max(building[1] for building in active)
            if max_h != current:
                current = max_h
                points.append((i,max_h))
     
        l = []
        for index, item in enumerate(points):
            if index < len(points)-1:
                a = item[0]
                b = item[1]
                elem = points[index+1]
                c = elem[0]
                if b != 0:
                    l.append((a,b,c))
        self.bl = l

