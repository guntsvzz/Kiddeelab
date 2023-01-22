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

def update():
    pass

pgzrun.go()