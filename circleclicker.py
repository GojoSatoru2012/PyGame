import pygame
#function to initialize
pygame.init()
screen = pygame.display.set_mode([500,500])
#variable for While loop
running = True
#defining colors
Red = (255, 0 , 0)
Blue = (0, 255, 0)
Green = (0, 0, 255)
Yellow = (150, 0, 150)
Purple = (150, 150, 0)
Orange = (150, 150, 150)
screen.fill(Orange)
class Circle:
    def __init__(self, color, pos, radius, thicness = 0):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.thicness = thicness
        self.scr = screen 
    def draw(self):
        pygame.draw.circle(self.scr, self.color, self.pos, self.radius, self.thicness)
    def growing(self, cg):
        self.radius += cg
        pygame.draw.circle(self.scr, self.color, self.pos, self.radius, self.thicness)
pos1 = (250, 250)
r = 69
yy = 5
pygame.draw.circle(screen, Red, pos1, r, yy)
pygame.display.update()
#creating multiple objects
obj1 = Circle
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
