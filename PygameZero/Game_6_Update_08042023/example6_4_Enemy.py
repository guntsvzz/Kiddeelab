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
WIDTH  = TILE_SIZE * number_column #x
HEIGHT = TILE_SIZE * number_row #y

## SPRITE PART
player = Actor('grassblock', anchor = (0,0))
player.pos = TILE_SIZE * 1, TILE_SIZE * 1

## ENEMY PART
enemy = Actor('blockermad',anchor=(-10,-10))
enemy.pos = 5 *TILE_SIZE, 3*TILE_SIZE #5,3
enemy.yv = -1
## MAP PART
maze_bg = 0 #default map
unlock = 0

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
    enemy.draw()

def update():
    pass

def enemy_moving(enemy):
    row    = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    if maze_bg == 0:
        row += enemy.yv
    if maze_bg == 2:
        column += enemy.yv

    material = map[maze_bg][row][column]
    tile = tiles[material]    
    if tile == 'path':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration = 0.1, pos = (x,y))
    else:
        enemy.yv *= -1

    if enemy.colliderect(player):
        print('You died')
        exit()

def on_key_down(key):
    global unlock, maze_bg
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
    print(column * TILE_SIZE)
    print(row * TILE_SIZE)

    try:
        material = map[maze_bg][row][column]
        print(material)
        tile = tiles[material]
        if tile == 'path':
            #Formate animate(sprite, duration, position)
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            if not toucingroom(x, y):
                animate(player, duration = 0.1, pos = (x,y))
            # print(f'x: {x} y: {y}')
        elif tile == 'keyblue':
            unlock += 1
            map[maze_bg][row][column] = 0
        elif tile == 'lock_blue' and unlock > 0:
            unlock -= 1
            map[maze_bg][row][column] = 0

        else:
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            toucingroom(x, y)
    except:
        print('Out of list')
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        toucingroom(x, y)
        
    enemy_moving(enemy)

def toucingroom(x_player, y_player):
    global maze_bg 
    ## ROOM 1 : LEFT to RIGHT
    if maze_bg == 0 and x_player == WIDTH: #1 to 2
        maze_bg = 1
        player.x = 0 * TILE_SIZE 
        enemy.pos = 5 * TILE_SIZE, 3 * TILE_SIZE
        return True
    ## ROOM 1 : BOTTOM to UP
    elif maze_bg == 0 and y_player == -1 * TILE_SIZE: #1 to 3
        maze_bg = 2
        player.y = 9 * TILE_SIZE 
        enemy.pos = 5 * TILE_SIZE, 7 * TILE_SIZE
        return True
    ## ROOM 2 : RIGHT to LEFT
    elif maze_bg == 1 and x_player == -1 * TILE_SIZE: #2 to 1
        maze_bg = 0
        player.x = 9 * TILE_SIZE 
        return True
    ## ROOM 3 : UP to BOTTOM
    elif maze_bg == 2 and y_player == HEIGHT: #3 to 1
        maze_bg = 0
        player.y = 0 * TILE_SIZE 
        return True
    
    return False

pgzrun.go()
