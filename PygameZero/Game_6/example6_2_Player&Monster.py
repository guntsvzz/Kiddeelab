import pgzrun
import pygame
import random
from maze_pattern import *

## TILE PART
TITLE = 'Game 6'
TILE_SIZE = 70
tiles = {
    0 : 'path',
    1 : 'wall'
}
maze = [
    #0  1  2  3  4  5  6  7  8  9  10 11
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1], #0
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1], #1
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1], #2
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], #3
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1], #4
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0], #5
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #6
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1], #7
    [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1], #8
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], #9
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #10
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #11
]
number_column = len(maze[0]) 
number_row    = len(maze)
WIDTH  = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row
## SPRITE PART
player = Actor('grassblock', anchor = (0,0))
player.pos = TILE_SIZE * 1, TILE_SIZE * 1

def draw():
    ##Tile draw
    for row in range(number_row):
        for column in range(number_column):
            x = column * TILE_SIZE 
            y = row * TILE_SIZE
            screen.blit('path', (x,y))
            material = maze[row][column]
            tile = tiles[material]
            if tile != 'path':
                screen.blit(tile, (x,y))
    ##Player draw
    player.draw()

def update():
    pass

def on_key_down(key):
    row    = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == key.UP or key == key.W:
        row -=1 
    if key == key.DOWN or key == key.S:
        row +=1 
    if key == key.LEFT or key == key.A:
        column -=1 
    if key == key.RIGHT or key == key.D:
        column +=1 
    ##CHECKING PATH WALKING
    material = maze[row][column]
    tile = tiles[material]
    
    if tile == 'path':
        #Formate animate(sprite,duration,position)
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        print(f'x: {x} y: {y}')
        animate(player, duration = 0.1, pos = (x,y))

pgzrun.go()
