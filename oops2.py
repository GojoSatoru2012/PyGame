class space():
    def __init__(self, planets, galaxy):
        self.planets = planets
        self.galaxy = galaxy
    def printinfo(self):
        print(self.planets, self.galaxy)
earth = space(8,100000000)
earth.printinfo() 