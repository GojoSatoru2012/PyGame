import  pygame 
game = True
pygame.init()
screen = pygame.display.set_mode((600, 600))
#filling the screen with a color
screen.fill("White")
pygame.display.update()
#shapes
class shapes():
    def __int__(self, color, size):
        self.color = color
        self.size = size
        self.rect_surf = screen
    def draw(self):
        self.rectdraw = pygame.draw.rect(self.rect_surf, self.color, self.size)
#creating objects
Red = shapes("red", (100,200,100,50))
Blue = shapes("blue", (250,300,150,100))
Purple = shapes("purple", (300,400,200,50))
#important part
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    Red.draw()
    Blue.draw()
    Purple.draw()
    pygame.display.update()
pygame.quit()
