import matplotlib.pyplot as plt

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
        self.bl += [(xmin, height, xmax)]

    # add a skyline to the current skyline
    def addSkyline(self, skyobj):
        print('addSkyline from skyline.py')
        print(self.bl)
        print(skyobj.getBuildingsList())
        self.bl += skyobj.getBuildingsList()
        print(self.bl)


    # do the intersection between skyobj and current skyline
    def intersecSkyline(self, skyobj):
        print('intersec de skyline.py')
        a = self.bl
        print('a:')
        print(a)

        b = skyobj.getBuildingsList()
        print('b:')
        print(b)
        result = []
        for k in a:
            if (k not in result) and (k in b):
                result.append(k)
        print('result:')
        print(result)
        self.bl = result

    # do the refelction of the current skyline
    def mirrorSkyline(self):
        print('mirrorSkyline de la skyline.py')
        print(self.bl)
        l = self.bl
        l.reverse()
        print(l)
        self.bl = l
        print('salgo de mirrorSkyline')

    # replicate the skyline n times
    def replicateSkyline(self, n):
        print('replicate de la skyline.py')
        l = (self.bl).copy()
        print('l')
        print(l)
        for k in range(n-1):
            print('dentro del for, k:')
            print(k)
            print('l:')
            print(l)
            print('self.bl:')
            print(self.bl)
            self.bl += l

    # shift skyline n positions to the right
    def shiftRight(self, n):
        l = []
        print('shiftRight en skyline.py')
        print('self.bl antes')
        print(self.bl)
        for k in self.bl:
            print(k)
            k = list(k)
            k[0] += n
            k[2] += n
            k = tuple(k)
            l.append(k)
            print(k)
        self.bl = l
        print('self.bl despues:')
        print(self.bl)


    # shift skyline n positions to the left
    def shiftLeft(self, n):
        l = []
        print('shiftLeft en skyline.py')
        print('self.bl antes')
        print(self.bl)
        for k in self.bl:
            print(k)
            k = list(k)
            k[0] -= n
            k[2] -= n
            k = tuple(k)
            l.append(k)
            print(k)
        self.bl = l
        print('self.bl despues:')
        print(self.bl)


    # ########PROCESSING########## #

    def plotProcessing(self):
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



    # ###########UTILS############ #

    
    
    def buildingArea(b):
        y = b[1]
        z = b[2]
        x = b[0]
        return y*(z-x)

    def random(n, h, w, xmin, xmax):
        seed = 53
        #TODO