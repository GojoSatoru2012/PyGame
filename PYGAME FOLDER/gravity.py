import pgzrun
import random
import time
TITLE = "Gravity ball"
WIDTH = 600
HEIGHT = 400
red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
color = (red,green,blue)
GRAVITY = 2000
class ball:
    def __init__(self, initialx, initialy):
        self.x = initialx
        self.y = initialy
        self.vx = 150
        self.vy = 0
        self.radius = 30
    def draw(self):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        color = (red,green,blue)
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, color)
b = ball(300,200)
def draw():
    #screen.clear()
    b.draw()
def waitclear():
    screen.clear()

def update(dt):
    #constant acceleration formulae
    uy = b.vy
    b.vy += GRAVITY * dt
    b.y += (uy + b.vy) * 0.5 * dt
    #detect and handle bouncing
    if b.y > HEIGHT - b.radius:
        b.y = HEIGHT - b.radius
        b.vy = - b.vy * 0.9
    #x compinent do not need have to have acelaration
    b.x += b.vx * dt
    if b.x > WIDTH - b.radius or b.x < b.radius:
        b.vx = -b.vx
def on_key_down(key):
    if key == keys.SPACE:
        b.vy =- 500
clock.schedule(waitclear, 3)
pgzrun.go()