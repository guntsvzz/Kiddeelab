import pgzrun
import pygame
import random

TITLE = 'Game 2 Flappy Birds'
WIDTH, HEIGHT = 500,800

birdSprite = Actor('bird1')
birdSprite.pos = 50,200
pipe_top = Actor('pipetop')
pipe_top.pos = 250,75
pipe_bottom = Actor('pipebottom')
pipe_bottom.pos = 250,725

def draw():
    screen.blit('background',(0,0))
    birdSprite.draw()
    pipe_top.draw()
    # pipe_bottom.draw()

def update():
    pass

pgzrun.go()