iimport pygame
import random
import time
from pygame.locals import *
pygame.init()
running = True
score = 0
scorefont = pygame.font.SysFont("sans serif", 40)
text=scorefont.render("Score ="+str(score), True, "yellow")
clock = pygame.time.Clock()
starting = time.time()
timefont = pygame.font.SysFont("Script", 20)

def background(bg):
    bg1  = pygame.image.load(bg)
    bg2 = pygame.transform.scale(bg1, (screen_width, screen_height))
    screen.blit(bg2, (0,0))
pygame.display.set_caption("Donot Litter")
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
class Bin(pygame.sprite.Sprite):
    def __init__(self, speed = 5):
        super().__init__()
        self.image = pygame.image.load("Trash.webp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self, key):
        if key[pygame.K_w]:
            self.rect.move_ip(0,- self.speed)
        if key[pygame.K_a]:
            self.rect.move_ip(- self.speed,0)
        if key[pygame.K_d]:
            self.rect.move_ip(+ self.speed,0)
        if key[pygame.K_s]:
            self.rect.move_ip(0,+ self.speed)
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
for i in range(20):
    obj1 = Plasticbag()
    obj1.rect.x = random.randint(30, 770)
    obj1.rect.y = random.randint(30, 770)
    notrec.add(obj1)
    all.add(obj1)
can = Bin()
all.add(can)
def startup():
    global running
    while running:
        global text
        global score
        global calculator
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        calculator = time.time()- starting
        if calculator >= 20:
            if score >= 10:
                text=scorefont.render("You win", True, "green")
            else:
                text=scorefont.render("You lose", True, "red")
            screen.blit(text, (400, 300))
        else:
            remaining = 60 - int(calculator)
            count = 60
            timing = timefont.render("Time:"+str(remaining),True,"white")
            screen.blit(timing, (20, 10))
            key1 = pygame.key.get_pressed()
            if key1[pygame.K_w]:
                can.rect.move_ip(0,- can.speed)
            if key1[pygame.K_a]:
                can.rect.move_ip(- can.speed,0)
            if key1[pygame.K_d]:
                can.rect.move_ip(+ can.speed,0)
            if key1[pygame.K_s]:
                can.rect.move_ip(0,+ can.speed)
            gcollide = pygame.sprite.spritecollide(can, allrec, True)
            bcollide = pygame.sprite.spritecollide(can, notrec, True)
            for i in gcollide:
                score += 1
                text=scorefont.render("Score ="+str(score), True, "yellow")
            for i in bcollide:
                score -= 5
                text=scorefont.render("Score ="+str(score), True, "yellow")
            background("background.jpg")
            screen.blit(text, (600, 10))
            screen.blit(timing, (20, 10))
            all.draw(screen)
        pygame.display.update()
startup()
pygame.quit() 
