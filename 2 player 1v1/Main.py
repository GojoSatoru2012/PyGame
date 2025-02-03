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
font3 = pygame.font.SysFont("Script", 65)
#variables 
fps = 60
speed = 50
bspeed = 10
Blubullet = []
Redbullet = []
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
            if self.rect.left <= BORDER.right or self.rect.right >= 850:
                self.rect.move_ip(-speed, 0)


Player1 = Player(plr1, 0, 40, 300)
Player2 = Player(plr2, 0, 600, 300)
plrgr = pygame.sprite.Group()
plrgr.add(Player1)
plrgr.add(Player2)
def Bullet():
    for bullet in Blubullet:
        pygame.draw.rect(screen, "red",bullet)
        bullet.x -= bspeed
    for bullet in Redbullet:
        pygame.draw.rect(screen, "blue",bullet)
        bullet.x += bspeed
def Damage():
    global plr1health
    global plr2health
    for bullet in Redbullet:
        if Player2.rect.colliderect(bullet):
            plr2health -=10
            Redbullet.remove(bullet)
    for bullet in Blubullet:
        if Player1.rect.colliderect(bullet):
            plr1health -=10
            Blubullet.remove(bullet)
    
bluhit = pygame.USEREVENT + 1
redhit = pygame.USEREVENT + 2
clock = pygame.time.Clock()
def adding():
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen,"black", BORDER)
    texthold = font1.render("Health: " + str(plr1health), 1, "Blue")
    texthold2 = font2.render("Health: " + str(plr2health), 1, "Red")
    screen.blit(texthold, (30,10))
    screen.blit(texthold2, (600,10))


def plrwin(text):
    text1 = font3.render(text, 1, "green")
    screen.blit(text1, (10, 250))
    pygame.display.update()
    pygame.time.delay(6000)
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_LSHIFT:
                bullet = pygame.Rect(Player1.rect.x + Player1.rect.width, Player1.rect.y + Player1.rect.height//2 - 2, 20, 10)
                Redbullet.append(bullet)
            if event.key == K_RSHIFT:
                bullet = pygame.Rect(Player2.rect.x, Player2.rect.y + Player2.rect.height//2 - 2, 20, 10)
                Blubullet.append(bullet)
        if event.type == redhit:
            plr1health -= 10
        if event.type == bluhit:
            plr2health -= 10
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
    Bullet()
    Damage()
    if plr2health == 0:
        hold = "Player1 Has Won The Game!"
        plrwin(hold)
        run = False
    if plr1health == 0:
        hold2 = "Player2 Has Won The Game!"
        plrwin(hold2)
        run = False
    pygame.display.update()
pygame.quit()
