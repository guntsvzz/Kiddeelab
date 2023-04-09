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
    
    def __init__(self, image_file, position, pipe_speed = 2):
        super().__init__(image_file)
        self.position = position
        if position == 'TOP':
            self.pos = (250,75)
        if position == 'BOTTOM':
            self.pos = (250,725)
        self.pipe_speed = pipe_speed

    def reset_pipes(self):
        pipe_shift = random.randint(-150,200)
        pipe_top.pos = WIDTH, 0 + pipe_shift
        pipe_bottom.pos = WIDTH, 650 + pipe_shift

    def update(self):
        pipe_top.x -= self.pipe_speed
        pipe_bottom.x -= self.pipe_speed
        if (pipe_top.x or pipe_bottom.x) <= 0:
            self.reset_pipes() 

birdSprite = Bird('bird1')
pipe_top = Pipe('pipetop', position = 'TOP')
pipe_bottom = Pipe('pipebottom', position = 'BOTTOM')

def draw():
    screen.blit('background',(0,0))
    birdSprite.draw()
    pipe_top.draw()
    pipe_bottom.draw()

def update():
    pipe_top.update()
    pipe_bottom.update()

pgzrun.go()