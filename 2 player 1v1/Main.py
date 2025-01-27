import pygame
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gojo vs Sukuna")
#colors
c1 = (255, 255, 255)
c2 = (160, 32, 240)
c3 = (255, 0, 0)
c4 = (0, 155, 155)
font1 = pygame.font.SysFont("Script", 30)
font2= pygame.font.SysFont("sans serif", 50)
#variables 
fps = 60
speed = 50
bspeed = 250
#images
plr1 = pygame.image.load("Player1.png")
plr2 = pygame.image.load("Player2.png")
bg = pygame.image.load("Background.webp")
bg = pygame.transform.scale(bg, (800, 600))
plr1health = 100
plr2health = 100
BORDER = pygame.Rect(825//2 - 5, 0, 10, 800)
class Player(pygame.sprite.Sprite):
    def __init__(self, image, angle, x, y):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (150,200)),angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def move1(self, speed):
        self.rect.move_ip(0,speed)
        if self.rect.top <= 0 or self.rect.bottom >= 620:
            self.rect.move_ip(0,-speed)
    
    def move2(self, speed, p):
        self.rect.x += speed
        if p == 1:
            if self.rect.left <= -20 or self.rect.right >= BORDER.left:
                self.rect.move_ip(-speed, 0)
        if p == 2:
            if self.rect.left <= BORDER.right or self.rect.right >= 800:
                self.rect.move_ip(-speed, 0)


Player1 = Player(plr1, 0, 40, 300)
Player2 = Player(plr2, 0, 600, 300)
plrgr = pygame.sprite.Group()
plrgr.add(Player1)
plrgr.add(Player2)
clock = pygame.time.Clock()
def adding():
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen,"black", BORDER)
    texthold = font1.render("Health: " + str(plr1health), 1, "Blue")
    texthold2 = font2.render("Health: " + str(plr2health), 1, "Red")
    screen.blit(texthold, (30,10))
    screen.blit(texthold2, (600,10))


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    keypressed = pygame.key.get_pressed()
    if keypressed[K_w]:
        Player1.move1(-speed)
    if keypressed[K_s]:
        Player1.move1(speed)
    if keypressed[K_UP]:
        Player2.move1(-speed)
    if keypressed[K_DOWN]:
        Player2.move1(speed)
    if keypressed[K_a]:
        Player1.move2(-speed, 1)
    if keypressed[K_d]:
        Player1.move2(speed, 1)
    if keypressed[K_RIGHT]: 
        Player2.move2(speed, 2)
    if keypressed[K_LEFT]:
        Player2.move2(-speed, 2)
    adding()
    plrgr.draw(screen)
    pygame.display.update()
