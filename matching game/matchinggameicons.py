import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("Red")
#loading images
subwaysurfer = pygame.image.load("subwaysurfers.png")
minecraft = pygame.image.load("sminecraft.webp")
cs2 = pygame.image.load("cs2.jpg")
templerun = pygame.image.load("templerun.avif")
roblox = pygame.image.load("Roblox.webp")
#original correct position 
dictionarygame = {"subwaysurfer", (150, 50),"minecraft", (150, 150),"roblox", (150, 250), "templerun", (150, 350), "cs2", (150, 450),}
#shuffling image position 
imagepos = list(dictionarygame)
random.shuffle(imagepos)
imagepos1 = {name: dictionarygame[imagepos[i]] for i, name in enumerate(dictionarygame)}
#display images
screen.blit(subwaysurfer, imagepos1["subwaysurfer"])
screen.blit(templerun, imagepos1["templerun"])
screen.blit(cs2, imagepos1["cs2"])
screen.blit(roblox, imagepos1["roblox"])
screen.blit(minecraft, imagepos1["minecraft"])
pygame.display.update