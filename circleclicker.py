import pygame
#function to initialize
pygame.init()
screen = pygame.display.set_mode([500,500])
#variable for While loop
running = True
#defining colors
Red = (255, 0 , 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Purple = (160, 32, 240)
Orange = (255, 165, 0)
White = (255, 255, 255)
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
obj1 = Circle(Red, pos1, r + 50, 7)
obj2 = Circle(Purple, pos1, r + 40, 7)
obj3 = Circle(Blue, pos1, r + 30, 7)
obj4 = Circle(Green, pos1, r + 20, 7)
obj5 = Circle(Orange, pos1, r + 15, 7)
obj6 = Circle(Yellow, pos1, r + 10, 7)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            obj1.draw()
            obj2.draw()
            obj3.draw()
            obj4.draw()
            obj5.draw()
            obj6.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            obj1.growing(3)
            obj2.growing(7)
            obj3.growing(5)
            obj4.growing(3)
            obj5.growing(2)
            obj6.growing(4)
        elif event.type == pygame.MOUSEMOTION:
            posi = pygame.mouse.get_pos()
            obj7 = Circle(White, posi, 6)
            obj7.draw()
            pygame.display.update()

pygame.quit()
