import pygame
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Gojo vs Sukuna")
#colors
c1 = (255, 255, 255)
c2 = (160, 32, 240)
c3 = (255, 0, 0)
c4 = (0, 155, 155)
font1 = pygame.font.SysFont("Script", 90)
font2= pygame.font.SysFont("sans serif", 90)
#variables 
fps = 60
speed = 80
bspeed = 250
#images
plr1 = pygame.image.load("Player1.webp")
plr2 = pygame.image.load("Player2.png")
bg = pygame.image.load("Background.webp")
plr1health = 100
plr2health = 100
rectangle1 = BORDER = pygame.Rect(600//2 - 5, 0, 10, 800)
class Player(pygame.sprite.Sprite):
    def __init__(self, image, angle, x, y):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (300,400)),angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

Player1 = Player(plr1, 270, 40, 300)
Player2 = Player(plr2, 90, 600, 300)
plrgr = pygame.sprite.Group()
plrgr.add(Player1)
plrgr.add(Player2)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    plrgr.draw(screen)
    pygame.display.update()
