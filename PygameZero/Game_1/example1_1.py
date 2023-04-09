import pygame
import pgzrun
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600
#Class Actor
monkeySprite = Actor('monkey1') #object
#object.variables
monkeySprite.pos = (WIDTH/2,HEIGHT/2) #tuple #pos = position
#object.method()

def draw():
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    monkeySprite.draw()

def movement():
    if keyboard.w or keyboard.up: #full
        monkeySprite.y = monkeySprite.y - 5 #full
    if keyboard.a or keyboard.left: #short
        monkeySprite.x -= 5 #short
    if keyboard.s or keyboard.down: #short
        monkeySprite.y += 5 #short
    if keyboard.d or keyboard.right: #short
        monkeySprite.x += 5 #short

def update():
    movement()

pgzrun.go()