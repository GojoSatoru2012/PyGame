import pygame
import random
clock = pygame.time.Clock()
from pygame.locals import *
running = True
def background(bg):
    bg1  = pygame.image.load(bg)
    bg2 = pygame.transform.scale(bg1, (screen_width, screen_height))
    screen.blit(bg2, (0,0))
pygame.init()
pygame.display.set_caption("Donot Litter")
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Trash.webp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
class Plasticbag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plasticbag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
class Recycle(pygame.sprite.Sprite):
    def __init__(self, recycled):
        super().__init__()
        self.image = pygame.image.load(recycled).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
Rlist = ["apple.webp", "can.png", "paperbag.png"]
allrec = pygame.sprite.Group()
notrec = pygame.sprite.Group()
all = pygame.sprite.Group()
#creating recycled items on the screen
for i in range(57):
    RandCho = Recycle(random.choice(Rlist))
    RandCho.rect.x = random.randint(30, 770)
    RandCho.rect.y = random.randint(30, 770)
    allrec.add(RandCho)
    all.add(RandCho)
for i in range(60):
    obj1 = Plasticbag()
    obj1.rect.x = random.randint(30, 770)
    obj1.rect.y = random.randint(30, 770)
    notrec.add(obj1)
    all.add(obj1)
can = Bin()
all.add(can)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background("background.jpg")
    all.draw(screen)
    pygame.display.update()
pygame.quit() mage, (40,60))
        self.rect = self.image.get_rect()

