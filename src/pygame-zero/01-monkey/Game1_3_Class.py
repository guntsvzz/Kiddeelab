import pygame
import pgzrun
import random
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600

class Sprite(Actor):
    monkeyimage = ['monkey1','monkey2']

    def __init__(self, image_file, pos = (WIDTH/2, HEIGHT/2)):
        super().__init__(image_file, pos)
        self.pos = pos

    def monkey_limit(self):
        if self.x >= WIDTH:
            self.x = WIDTH
        if self.x <= 0:
            self.x = 0
        if self.y >= HEIGHT:
            self.y = HEIGHT
        if self.y <= 0:
            self.y = 0

    def moving(self): #non-smoothing
        self.monkey_limit()
        if self.image == Sprite.monkeyimage[0]: #check
            self.image = Sprite.monkeyimage[1] #change
        elif self.image == Sprite.monkeyimage[1]: #check
            self.image = Sprite.monkeyimage[0] #change
            
    def movement(self):
        if keyboard.w or keyboard.up: #full
            monkeySprite.y = monkeySprite.y - 5 #full
            self.moving()
        if keyboard.a or keyboard.left: #short
            monkeySprite.x -= 5 #short
            self.moving()
        if keyboard.s or keyboard.down: #short
            monkeySprite.y += 5 #short
            self.moving()    
        if keyboard.d or keyboard.right: #short
            monkeySprite.x += 5 #short
            self.moving()

class Fruit(Actor):
    def __init__(self, image_file, pos = (random.randint(0,WIDTH),0)):
        super().__init__(image_file, pos)
        self.pos = pos

    def spawn(self):
        self.y += 6
        if self.y > HEIGHT:
            self.pos = (random.randint(0,WIDTH),0)

monkeySprite = Sprite('monkey1')
bananaSprite = Fruit('banana')
spiderSprite = Fruit('spider')

def draw():
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    monkeySprite.draw()
    bananaSprite.draw()
    spiderSprite.draw()

def update(): #1/60 second
    monkeySprite.movement()
    bananaSprite.spawn()
    spiderSprite.spawn()

pgzrun.go()