import pgzrun
import pygame
import random

TITLE = 'Game 2 Flappy Birds'
WIDTH, HEIGHT = 500, 800

birdSprite = Actor('bird1')
birdSprite.pos = 50,200
pipe_top = Actor('pipetop')
pipe_top.pos = WIDTH,75
pipe_bottom = Actor('pipebottom')
pipe_bottom.pos = WIDTH,725
pipe_speed = 3 #speed
birdSprite.vy = 0
GRAVITY = 0.3
FLAP_VELOCITY = -5

def draw():
    screen.blit('background',(0,0))
    birdSprite.draw()
    pipe_top.draw()
    pipe_bottom.draw()

def reset_pipes():
    pipe_shift = random.randint(-150,200)
    pipe_top.pos = WIDTH, 0 + pipe_shift
    pipe_bottom.pos = WIDTH, 650 + pipe_shift

def update():
    pipe_top.x -= pipe_speed
    pipe_bottom.x -= pipe_speed
    if (pipe_top.x or pipe_bottom.x) <= 0:
        reset_pipes() 
    birdSprite.vy += GRAVITY
    birdSprite.y += birdSprite.vy
    print(f'Velocity : {birdSprite.vy:.5}')
    print(f'Position : {birdSprite.y:.5}')
    
    if birdSprite.vy <-3:
        birdSprite.image = 'bird2'
    else:
        birdSprite.image = 'bird1'

def on_key_down(key):
    if key == key.UP:
        birdSprite.vy = FLAP_VELOCITY

pgzrun.go()