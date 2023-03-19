import pgzrun
import pygame
import random
## TILE PART
TITLE = 'Game 6'
TILE_SIZE = 70
tiles = {
    0 : 'path',
    1 : 'wall'
}
maze = [
    #0  1  2  3  4  5  6  7  8  9  10 11 12
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], #1
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1], #2
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #3
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1], #4
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1], #5
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], #6
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], #7
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #8
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #9
]
number_column = len(maze[0]) 
number_row    = len(maze)
WIDTH  = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row
## SPRITE PART

def draw():
    for row in range(number_row):
        for column in range(number_column):
            x = column * TILE_SIZE 
            y = row * TILE_SIZE
            screen.blit('path', (x,y))
            material = maze[row][column]
            tile = tiles[material]
            if tile != 'path':
                screen.blit(tile, (x,y))


def update():
    pass

pgzrun.go()
