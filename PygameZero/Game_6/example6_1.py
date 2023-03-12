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
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
number_column = len(maze[0]) 
number_row    = len(maze)
WIDTH  = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row
## SPRITE PART

def draw():
    pass

def update():
    pass

pgzrun.go()
