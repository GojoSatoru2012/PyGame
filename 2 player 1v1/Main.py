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