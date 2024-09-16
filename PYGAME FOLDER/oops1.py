class games():
    def __init__(self,genre,rating):
        print("Ratings and genre")
        self.genre = genre
        self.rating = rating
    def printinfo(self):
        print(self.genre, self.rating)
Roblox = games("all genre","4.5")
Mugen = games("fighting","3.9")
Roblox.printinfo()
Mugen.printinfo()