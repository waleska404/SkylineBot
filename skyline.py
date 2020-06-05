class Skyline:
    def __init__(self, id, xmin, height, xmax):
        b1 = (xmin, height, xmax)
        bl = [ed1]
        self.id = id
        self.bl = bl  # bl = buildings list

    def getBuildingsList(self):
        return bl

    def getID(self):
        return id

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

    # UTILS #
    def listIntersection(a, b):
        result = []
        for i in a:
            if (i not in result) and (i in b):
                result.append(i)
        return result
