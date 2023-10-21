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
birdSprite.status = True
birdSprite.score = 0
#game_state
game_state = 'main'

def draw():
    screen.blit('background',(0,0))

    def restart():
        global game_state 
        screen.draw.text('Press space to restart',center = (WIDTH/2, HEIGHT/2+50), color = (255,0,0), fontsize = 40)
        if keyboard.space:
            game_state = 'play'
            birdSprite.status = True
            birdSprite.score = 0
            birdSprite.pos = 50,200
            pipe_top.pos = WIDTH,75
            pipe_bottom.pos = WIDTH,725
            print(f'Game Status : {game_state}')

    if game_state == 'main':
        screen.draw.text('Flappy Bird',center = (WIDTH/2, HEIGHT/2), color = (255,0,0), fontsize = 40)
        restart()
    elif game_state == 'lose':
        screen.draw.text('You lose',center = (WIDTH/2, HEIGHT/2), color = (255,0,0), fontsize = 40)
        restart()
    elif game_state == 'win':
        screen.draw.text('You win',center = (WIDTH/2, HEIGHT/2), color = (255,0,0), fontsize = 40)
        restart()
    elif game_state == 'play':
        birdSprite.draw()
        pipe_top.draw()
        pipe_bottom.draw()
        screen.draw.text('Score: ' + str(birdSprite.score), (15, 10), color=(255, 255, 255), fontsize=40)

def reset_pipes():
    pipe_shift = random.randint(-150,200)
    pipe_top.pos = WIDTH, 0 + pipe_shift
    pipe_bottom.pos = WIDTH, 650 + pipe_shift
    birdSprite.score +=1

def update():
    global game_state
    if game_state == 'play':
        #pipe
        pipe_top.x -= pipe_speed
        pipe_bottom.x -= pipe_speed
        if (pipe_top.x or pipe_bottom.x) <= 0:
            reset_pipes() 
        #bird
        birdSprite.vy += GRAVITY
        birdSprite.y += birdSprite.vy
        print(f'Velocity : {birdSprite.vy:.5}')
        print(f'Position : {birdSprite.y:.5}')
        #animation 
        if birdSprite.vy <-3:
            birdSprite.image = 'bird2'
        else:
            birdSprite.image = 'bird1'
        #colliderect
        if birdSprite.colliderect(pipe_bottom) or birdSprite.colliderect(pipe_top) or \
            birdSprite.y > HEIGHT or birdSprite.y < 0 :
            birdSprite.image = 'birddead'
            birdSprite.status = False
            game_state = 'lose'
        #win 
        if birdSprite.score >= 10:
            game_state = 'win' 

def on_key_down(key):
    if key == key.UP and birdSprite.status == True:
        print('Up')
        birdSprite.vy = FLAP_VELOCITY

pgzrun.go()
