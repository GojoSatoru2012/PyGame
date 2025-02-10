import pygame
import random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
#variaqbles
fps = 60
screen = pygame.display.set_mode((864,600))
pygame.display.set_caption("Flappy Bird")
font1 = pygame.font.SysFont("Sans Serif", 30)
gs = 0
ss = 20
fly = False
gameover = False
pipegap = 5
pipefrequency = 1500
last_pipe = pygame.time.get_ticks() - pipefrequency
score = 0
passpipe = False
#images
bg = pygame.image.load("bg.png")
bround = pygame.image.load("ground.png")
restart = pygame.image.load("restart.png")
run = True
class bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
          bd = pygame.image.load(f"bird{i}.png")
          self.images.append(bd)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y] 
        self.vel = 0
        self.clicked = False
    def update(self):  
        if fly == True:
            self.vel += 0.5
            if self.vel > 2:
                self.vel = 2
            if self.rect.bottom < 600:
               self.rect.y += int(self.vel)
        if gameover == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True
                self.vel = -2
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False
            #handling animation  
            flap_cd = 5
            self.counter += 1
            if self.counter > flap_cd:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
class pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y - int(pipegap / 2)]
        elif pos == -1:
            self.rect.topleft = [x,y + int(pipegap / 2)]
    def update(self):
        self.rect.x -= ss
        if self.rect.right < 0:
            self.kill()

flappy = bird(100, 300)       
bf = pygame.sprite.Group()
bf.add(flappy)   

while run:
    clock.tick(fps)
    screen.blit(bg, (0,0))
    bf.draw(screen)
    bf.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         run = False
        if event.type == pygame.MOUSEBUTTONDOWN and fly == False and gameover == False:
            fly = True
    pygame.display.update()
pygame.quit()
