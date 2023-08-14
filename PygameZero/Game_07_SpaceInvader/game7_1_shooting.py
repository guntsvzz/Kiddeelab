import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (200,50)
import pgzrun, pygame, random

#resolution is in pixels
WIDTH, HEIGHT = 500, 800
TITLE = 'Space Invader'

bullets =[]

class Player(Actor):
    #properties/ variable
    def __init__(self, image_file, pos):
        super().__init__(image_file, pos)
        self.score = 0
        
    #function/ method
    def keybutton(self):
        #setting moving
        if keyboard.w:
            self.y -= 5
        if keyboard.s:
            self.y += 5
        if keyboard.a:
            self.x -= 5
        if keyboard.d:
            self.x += 5
    
        #setting boundary
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

class Bullet(Actor):
    #properties/ variable
    def __init__(self, image_file):
        super().__init__(image_file)
        self.is_reloading = False
        self.amount = 10

galagaSprite = Player('galaga', pos = (WIDTH/2, 550))

def on_key_down(key):
    if key == key.SPACE:
        bullets.append(Bullet('laserred'))
        bullets[-1].pos = galagaSprite.pos

def drawbullets():
    for bullet in bullets: 
        bullet.draw()

def updatedbullet():
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet) #specific value
        else:
            bullet.y -= 10

def draw():
    # screen.blit('galagabg', (0,0))
    screen.clear()
    galagaSprite.draw()
    drawbullets()

def update():
    galagaSprite.keybutton()
    updatedbullet()

pgzrun.go()