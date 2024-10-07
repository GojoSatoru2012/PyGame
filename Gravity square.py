import pgzrun
import random
import time
game = True
TITLE = "Gravity square"
WIDTH = 600
HEIGHT = 400
red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
color = (red,green,blue)
GRAVITY = 2000
class rectangle:
    def __init__(self, initialx, initialy):
        self.x = initialx
        self.y = initialy
        self.vx = 150
        self.vy = 0
        self.size = 30
        #self.height = 30
    def draw(self):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        color = (red,green,blue)
        pos = (self.x, self.y)
        screen.draw.filled_rect(Rect(pos, (self.size, self.size)), color)
r = rectangle(400,200)
def draw():
    r.draw()
def waitclear():
    screen.clear()

def update(dt):
    #constant acceleration formula
    uy = r.vy
    r.vy += GRAVITY * dt
    r.y += (uy + r.vy) * 0.5 * dt
    #detect and handle bouncing
    if r.y > HEIGHT - r.size:
        r.y = HEIGHT - r.size
        r.vy = - r.vy * 0.9
    #x compinent do not need have to have acelaration
    r.x += r.vx * dt
    if r.x > WIDTH - r.size or r.x < r.size:
        r.vx = -r.vx
def on_key_down(key):
    if key == keys.SPACE:
        r.vy =- 500
    clock.schedule(waitclear, 3)
pgzrun.go()