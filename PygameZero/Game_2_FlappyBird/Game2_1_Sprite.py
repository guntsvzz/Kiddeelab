import pgzrun
import pygame
import random

TITLE = 'Game 2 Flappy Birds'
WIDTH, HEIGHT = 500,800

class Bird(Actor):
    def __init__(self, image_file, pos = (50,200)):
        super().__init__(image_file, pos)
        self.pos = pos

class Pipe(Actor):
    def __init__(self, image_file, position):
        super().__init__(image_file)
        self.position = position
        if position == 'TOP':
            self.pos = (250,75)
        if position == 'BOTTOM':
            self.pos = (250,725)

birdSprite = Bird('bird1')
pipe_top = Pipe('pipetop', position = 'TOP')
pipe_bottom = Pipe('pipebottom', position = 'BOTTOM')

def draw():
    screen.blit('background',(0,0))
    birdSprite.draw()
    pipe_top.draw()
    pipe_bottom.draw()

def update():
    pass

pgzrun.go()