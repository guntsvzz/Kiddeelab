import pgzrun
import pygame
import random

TITLE = 'Game 2 Flappy Birds'
WIDTH, HEIGHT = 500,800


class Bird(Actor):

    GRAVITY = 0.3
    FLAP_VELOCITY = -5

    def __init__(self, image_file, pos = (50,200)):
        super().__init__(image_file, pos)
        self.pos = pos
        self.vy = 0

    def update(self):
        self.vy += Bird.GRAVITY
        self.y += self.vy
        print(f'Velocity : {self.vy:.5}')
        print(f'Position : {self.y:.5}')
        
        if self.vy <-3:
            self.image = 'bird2'
        else:
            self.image = 'bird1'

class Pipe(Actor):
    
    def __init__(self, image_file, position, pipe_speed = 3):
        super().__init__(image_file)
        self.position = position
        if position == 'TOP':
            self.pos = (250,75)
        if position == 'BOTTOM':
            self.pos = (250,725)
        self.pipe_speed = pipe_speed

    def reset_pipes(self, shift):
        if self.position == 'TOP':
            self.pos = WIDTH, 0 + shift
        if self.position == 'BOTTOM':
            self.pos = WIDTH, 650 + shift

    def update(self, shift):
        self.x -= self.pipe_speed
        if self.x <= 0:
            self.reset_pipes(shift) 

birdSprite = Bird('bird1')
pipe_top = Pipe('pipetop', position = 'TOP')
pipe_bottom = Pipe('pipebottom', position = 'BOTTOM')

def draw():
    screen.blit('background',(0,0))
    birdSprite.draw()
    pipe_top.draw()
    pipe_bottom.draw()

def on_key_down(key):
    if key == key.UP:
        birdSprite.vy = Bird.FLAP_VELOCITY

def update():
    pipe_shift = random.randint(-150,200)
    birdSprite.update()
    pipe_top.update(pipe_shift)
    pipe_bottom.update(pipe_shift)

pgzrun.go()