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
while run:
    clock.tick(fps)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         run = False
    pygame.display.update()
pygame.quit()