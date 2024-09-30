import  pygame 
game = True
pygame.init()
screen = pygame.display.set_mode((600, 600))
#filling the screen with a color
screen.fill("White")
pygame.display.update()
#shapes
class circles():
    def __init__(self, color, position, radius):
        self.color = color
        self.radius = radius
        self.position = position
        self.circle_surf = screen
    def draw(self):
        pygame.draw.circle(self.circle_surf, self.color, self.position, self.radius)
#creating objects
Red = circles("red", (100, 200), 33)
Blue = circles("blue", (200, 300), 40)
Purple = circles("purple", (300, 400), 45)
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
