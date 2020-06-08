import matplotlib.pyplot as plt
import datetime


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
        sum = 0
        for k in self.bl:
            sum += buildingArea(k)
        return sum

    # returns the skyline's height
    def getHeight(self):
        max = 0
        for k in self.bl:
            if k[1] > max:
                max = k[1]
        return max


    # ########OPERATIONS########## #

    # add a building to the current skyline
    def addBuilding(self, xmin, height, xmax):
        print('entro en addBuilding')
        self.bl += [(xmin, height, xmax)]
        print('salgo de addBuilding')

    # add a skyline to the current skyline
    def addSkyline(self, skyobj):
        #print('addSkyline from skyline.py')
        #print(self.bl)
        #print(skyobj.getBuildingsList())
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

        #print(self.bl)


    # return the intersection between skyobj and current skyline
    def intersecSkyline(self, skyobj):
        print('ENTRO intersec de skyline.py')
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
      
        edges1 = (sum(edges1,[])) #sorting and flatening the list of building edges
        #print(edges1)

        edges2.extend([building[0],building[2]] for building in bl2)
        edges2 = (sum(edges2,[])) #sorting and flatening the list of building edges
        #print(edges2)

        edaux = edges1 + edges2
        edaux = sorted(edaux)
 
        #print(edaux)
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
                #print('ENTRO EN NOT ACTIVE')
                #if there is no active buildings, highest point is 0
                current = 0
                points.append((i,0))
                continue
            min_h = min(building[1] for building in active)
            min_ed = i
            
            if min_h != current:
            #if current highest point is lower then highest point of current active buildings change current highest point
                current = min_h
                points.append((i,min_h))

        #print('POINTS:')
        last = edges[-1]
        points.append((last, 0))
        print(points)
        l = []
        for index, item in enumerate(points):
            if index < len(points)-1:
                a = item[0]
                b = item[1]
                elem = points[index+1]
                c = elem[0]
                if b != 0:
                    l.append((a,b,c))

        #print(l)
        elem = l[0]
        l.pop(0)
        s = Skyline('null',elem[0],elem[1],elem[2])
        for k in l:
            s.addBuilding(k[0],k[1],k[2])
        
        lr = s.getBuildingsList()
        return s  



        

    # do the refelction of the current skyline
    def mirrorSkyline(self):
        #print('mirrorSkyline de la skyline.py')
        l = (self.bl)
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

        self.bl = l2




    # replicate the skyline n times
    def replicateSkyline(self, n):
        #print('replicate de la skyline.py')
        
        l = (self.bl).copy()
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
        #print('AMPLITUD DEL SKYLINE')
        #print(w)
        
        #print('l')
        #print(l)

        for k in range(n-1):
            laux = []
            #print('dentro del for, k:')
            #print(k)
            #print('l:')
            #print(l)
            #print('self.bl:')
            #print(self.bl)
            #para cada elemento de l aumentarle la amplitud correspndiente
            for j in l:
                j = list(j)
                j[0] += w
                j[2] += w
                j = tuple(j)
                laux.append(j)
            w = w + ampOrig
            #print('l:')
            #print(l)
            self.bl += laux

    # shift skyline n positions to the right
    def shiftRight(self, n):
        l = []
        #print('shiftRight en skyline.py')
        #print('self.bl antes')
        #print(self.bl)
        for k in self.bl:
            #print(k)
            k = list(k)
            k[0] += n
            k[2] += n
            k = tuple(k)
            l.append(k)
            #print(k)
        self.bl = l
        #print('self.bl despues:')
        #print(self.bl)


    # shift skyline n positions to the left
    def shiftLeft(self, n):
        l = []
        #print('shiftLeft en skyline.py')
        #print('self.bl antes')
        #print(self.bl)
        for k in self.bl:
            #print(k)
            k = list(k)
            k[0] -= n
            k[2] -= n
            k = tuple(k)
            l.append(k)
            #print(k)
        self.bl = l
        #print('self.bl despues:')
        #print(self.bl)


    # ########PROCESSING########## #

    def plotProcessing(self):
        if self.id == 'null':
            #print('entra if self id = null')
            id = str(datetime.datetime.now())
            id = id.replace(" ","")
            id = id.replace(".","")
            id = id.replace(":","")
            id = id.replace("-","")
            #print(id)
            self.id = id
        #print(self.id)
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
        #print('antes del clear')
        plt.clf()
        #print('despues del clear')



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
    
    def buildingArea(b):
        y = b[1]
        z = b[2]
        x = b[0]
        return y*(z-x)

    def random(n, h, w, xmin, xmax):
        seed = 53
        #TODO

    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            # If the current value we're looking at is larger than the pivot
            # it's in the right place (right side of pivot) and we can move left,
            # to the next element.
            # We also need to make sure we haven't surpassed the low pointer, since that
            # indicates we have already moved all the elements to their correct side of the pivot
             while low <= high and self.graterEq(array[high],pivot):
                high = high - 1

            # Opposite process of the one above
             while low <= high and self.lowerEq(array[low],pivot):
                low = low + 1

            # We either found a value for both high and low that is out of order
            # or low is higher than high, in which case we exit the loop
             if low <= high:
                array[low], array[high] = array[high], array[low]
                # The loop continues
             else:
                # We exit out of the loop
                break

        array[start], array[high] = array[high], array[start]

        return high

    def quickSort(self, array, start, end):
        if start >= end:
            return

        p = self.partition(array, start, end)
        self.quickSort(array, start, p-1)
        self.quickSort(array, p+1, end)


    def sortSkyline(self):
        length = len(self.bl)
        bl = self.bl
        self.quickSort(bl, 0, length-1)
    
    def noOverlapping(self):
        buildings = self.bl
        edges = []
        edges.extend([building[0],building[2]] for building in buildings)
        print(edges)
        edges = sorted(sum(edges,[])) #sorting and flatening the list of building edges
        print(edges)
 
        current = 0
        points = []
  
        for i in edges:
            active = []
            active.extend(building for building in buildings if (building[0] <= i and building[2] > i)) 
            #current observed point is within borders of these buildings (active buildings)
            print(i,active)
            if not active: 
                #if there is no active buildings, highest point is 0
                current = 0
                points.append((i,0))
                continue
            max_h = max(building[1] for building in active)
            if max_h != current:
                #if current highest point is lower then highest point of current active buildings change current highest point
                current = max_h
                points.append((i,max_h))
     
        print(points)
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

