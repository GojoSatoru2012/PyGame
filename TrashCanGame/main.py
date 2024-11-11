import pygame
import random
from pygame.locals import *
def background(bg):
    bg1  = pygame.image.load(bg)
    bg2 = pygame.transform.scale(bg1, (screen_width, screen_height))
    screen.blit(bg2, (0,0))
pygame.init()
pygame.display.set_caption("Donot Litter")
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Trash.webp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
class Plasticbag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plasticbag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()

