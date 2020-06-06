import matplotlib.pyplot as plt

class Skyline:

    def __init__(self, id, xmin, height, xmax):
        b1 = (xmin, height, xmax)
        bl = [b1]
        self.id = id
        self.bl = bl  # bl = buildings list

    # ##########GETTERS########### #

    # returns the skyline's buildings list
    def getBuildingsList(self):
        return bl

    # returns the skyline's id
    def getID(self):
        return id

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
        self.bl += [(xmin, xmax, height)]

    # add a skyline to the current skyline
    def addSkyline(self, skyobj):
        self.bl += skyobj.getBuildingsList()

    # do the intersection between skyobj and current skyline
    def intersecSkyline(self, skyobj):
        bl2 = skyobj.getBuildingsList()
        self.bl = listIntersection(self.bl, bl2)

    # do the refelction of the current skyline
    def mirrorSkyline(self):
        self.bl = self.bl.reverse()

    # replicate the skyline n times
    def replicateSkyline(self, n):
        for k in range(n):
            self.bl += self.bl

    # shift skyline n positions to the right
    def shiftRight(self, n):
        for k in self.bl:
            k[0] += n

    # shift skyline n positions to the left
    def shiftLeft(self, n):
        for k in self.bl:
            k[0] -= n

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

    # returns the intersection of lists a and b
    def listIntersection(a, b):
        result = []
        for k in a:
            if (k not in result) and (k in b):
                result.append(k)
        return result
    
    def buildingArea(b):
        y = b[1]
        z = b[2]
        x = b[0]
        return y*(z-x)