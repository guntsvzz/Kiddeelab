import pgzrun
import pygame
import random
from maze_pattern import *

## TILE PART
TITLE = 'Game 6'
TILE_SIZE = 70
tiles = {
    0 : 'path',
    1 : 'wall',
    2 : 'lock_blue',
    3 : 'keyblue'
}
number_column = 10
number_row    = 10
WIDTH  = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row

## SPRITE PART
player = Actor('grassblock', anchor = (0,0))
player.pos = TILE_SIZE * 1, TILE_SIZE * 1

## MAP PART
maze_bg = 0 #default map

def draw():
    ##Tile draw
    def room(maze_bg = 0):
        for row in range(number_row):
            for column in range(number_column):
                x = column * TILE_SIZE 
                y = row * TILE_SIZE
                screen.blit('path', (x,y))
                material = map[maze_bg][row][column]
                tile = tiles[material]
                if tile != 'path':
                    screen.blit(tile, (x,y))

    room(maze_bg) #default = 0
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
    material = map[maze_bg][row][column]
    tile = tiles[material]
    if tile == 'path':
        #Formate animate(sprite, duration, position)
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        if not toucingroom(x, y):
            animate(player, duration = 0.1, pos = (x,y))
        print(f'x: {x} y: {y}')
        
def toucingroom(x_player, y_player):
    global maze_bg 
    ## ROOM 1 : LEFT to RIGHT
    if maze_bg == 0 and x_player == 9 * TILE_SIZE: #1 to 2
        maze_bg = 1
        player.x = 0 * TILE_SIZE 
        return True
    ## ROOM 1 : BOTTOM to UP
    elif maze_bg == 0 and y_player == 0 * TILE_SIZE: #1 to 3
        maze_bg = 2
        player.y = 9 * TILE_SIZE 
        return True
    ## ROOM 2 : RIGHT to LEFT
    elif maze_bg == 1 and x_player == 0 * TILE_SIZE: #2 to 1
        maze_bg = 0
        player.x = 9 * TILE_SIZE 
        return True
    ## ROOM 3 : UP to BOTTOM
    elif maze_bg == 2 and y_player == 9 * TILE_SIZE: #3 to 1
        maze_bg = 0
        player.y = 0 * TILE_SIZE 
        return True
    return False

pgzrun.go()
