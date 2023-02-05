import pygame
import pgzrun
import random
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600

#Class Actor
monkeyimage = ['monkey1','monkey2']
#object = class()
monkeySprite = Actor('monkey1') #object
#object.variables
monkeySprite.pos = (WIDTH/2,HEIGHT/2) #tuple #pos = position
#object.method()
bananaSprite = Actor('banana')
bananaSprite.pos = (random.randint(0,WIDTH),0)
spiderSprite = Actor('spider')
spiderSprite.pos = (random.randint(0,WIDTH),0)


def draw():
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    monkeySprite.draw()
    bananaSprite.draw()
    spiderSprite.draw()

def moving(): #non-smoothing
    if monkeySprite.image == monkeyimage[0]: #check
        monkeySprite.image = monkeyimage[1] #change
    elif monkeySprite.image == monkeyimage[1]: #check
        monkeySprite.image = monkeyimage[0] #change

def monkey_limit():
    if monkeySprite.x >= WIDTH:
        monkeySprite.x = WIDTH
    if monkeySprite.x <= 0:
        monkeySprite.x = 0
    if monkeySprite.y >= HEIGHT:
        monkeySprite.y = HEIGHT
    if monkeySprite.y <= 0:
        monkeySprite.y = 0

def movement():
    if keyboard.w or keyboard.up: #full
        monkeySprite.y = monkeySprite.y - 5 #full
        moving()
    if keyboard.a or keyboard.left: #short
        monkeySprite.x -= 5 #short
        moving()
    if keyboard.s or keyboard.down: #short
        monkeySprite.y += 5 #short
        moving()    
    if keyboard.d or keyboard.right: #short
        monkeySprite.x += 5 #short
        moving()

def bananaSpawn():
    bananaSprite.y += 6
    if bananaSprite.y > HEIGHT:
        bananaSprite.x = random.randint(0,WIDTH)
        bananaSprite.y = 0
   
def spiderSpawn():
    spiderSprite.y += 6
    if spiderSprite.y > HEIGHT:
        spiderSprite.pos = (random.randint(0,WIDTH),0)
   

def update(): #1/60 second
    movement()
    monkey_limit()
    bananaSpawn()
    spiderSpawn()

pgzrun.go()