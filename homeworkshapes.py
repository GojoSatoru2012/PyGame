import  pygame 
game = True
pygame.init()
screen = pygame.display.set_mode((600, 600))
#filling the screen with a color
screen.fill("White")
pygame.display.update()
#shapes
class circles():
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.circle_surf = screen
    def draw(self):
        self.circledraw = pygame.draw.circle(self.circle_surf, self.color, self.size)
#creating objects
Red = circles("red", (100,200,200,50))
Blue = circles("blue", (250,300,200,100))
Purple = circles("purple", (300,500,200,50))
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