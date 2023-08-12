import pgzrun
import random
from pattern_mazes import *

TILE = {
    0 : 'path',
    1 : 'wall',
    2 : 'key_yellow',
    3 : 'lock_yellow',
    4 : 'keyred',
    5 : 'lock_red',
    6 : 'keygreen',
    7 : 'lock_green',
    8 : 'keyblue',
    9 : 'lock_blue'

}
# print(tiles[0],tiles[1])
# MAIN[maps.room] = [A, B, C, D, E, F]
# MAIN[maps.room] = [
#     #0 1 2 3 4 5 6 7
#     [1,1,1,1,1,1,5,1], #0
#     [1,0,0,0,1,1,0,1], #1
#     [1,0,1,0,0,0,0,1], #2
#     [1,0,0,1,0,2,0,1], #3
#     [1,1,0,1,1,1,0,1], #4
#     [4,0,0,0,1,1,0,1], #5
#     [0,0,1,1,0,1,0,3], #6
#     [1,0,1,0,0,0,0,1], #7
# ] #8 rows, 6 columns
number_column = len(MAIN[0][0]) #len(MAZE[0]) #changable
number_row = len(MAIN[0]) #len(MAZE) #changable

TILE_SIZE = 70
WIDTH = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row

#class : map, player, enemy
class Map: #screen.blit
    def __init__(self, tile_size, num_row, num_column, MAIN, tile):
        self.tile_size = tile_size
        self.num_row = num_row
        self.num_column = num_column
        self.MAIN = MAIN
        self.tile = tile
        self.room = 0
    def generate(self): #generating a map 
        for row in range(self.num_row): 
            for column in range(self.num_column):
                #drawing path
                # print(row, column)
                x = self.tile_size * column
                y = self.tile_size * row
                screen.blit('path',(x,y))
                #drawing walls
                material = self.MAIN[self.room][row][column]
                t = self.tile[material]
                if t != 'path': #!= not equal
                    screen.blit(t,(x,y))

class Player(Actor):
    def __init__(self, image_file, anchor = (0,0), pos = (1*TILE_SIZE,7*TILE_SIZE)):
        super().__init__(image_file, anchor, pos)
        self.anchor = anchor
        self.pos = pos

class Enemy(Actor):
    def __init__(self, image_file, anchor = (-10,-10), pos = (1*TILE_SIZE,1*TILE_SIZE)):
        super().__init__(image_file, anchor, pos)
        self.anchor = anchor
        self.pos = pos

maps = Map(TILE_SIZE, number_row, number_column, MAIN, TILE)
player = Player('grassblock')
enemy = Enemy('blockermad')
keys = []

def on_key_down(key): #for toggle keyboard
    global MAIN, keys, maps
    row = int(player.y/TILE_SIZE) #0,1,2,3,4,6,
    column = int(player.x/TILE_SIZE) #1,2,3,4,5,6,7,8
    if key == key.UP or key ==key.W:
        row -=1
    if key == key.DOWN or key ==key.S:
        row +=1
    if key == key.LEFT or key ==key.A:
        column -=1
    if key == key.RIGHT or key ==key.D:
        column +=1

    try: #checking path to move
        x = column*TILE_SIZE
        y = row*TILE_SIZE
        print(f'Row={row}, Column={column}')
        print(f'x={x}, y={y}')
        material = MAIN[maps.room][row][column]

        if (TILE[material] == 'path') and (0 <= row <= number_row) and (0 <= column <= number_column):
            animate(player, duration = 0.1, pos = (x,y))
            # print('move')
        elif (TILE[material] == 'key_yellow'): #pick up the 
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.append('yellow_key')
        elif (TILE[material] == 'lock_yellow') and ('yellow_key' in keys):
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.remove('yellow_key')
        elif (TILE[material] == 'keyred'): #pick up the 
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.append('keyred')
        elif (TILE[material] == 'lock_red') and ('keyred' in keys):
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.remove('keyred')
        elif (TILE[material] == 'keygreen'): #pick up the 
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.append('keygreen')
        elif (TILE[material] == 'lock_green') and ('keygreen' in keys):
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.remove('keygreen')
        elif (TILE[material] == 'keyblue'): #pick up the 
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.append('keyblue')
        elif (TILE[material] == 'lock_blue') and ('keyblue' in keys):
            animate(player, duration = 0.1, pos = (x,y))
            MAIN[maps.room][row][column] = 0 
            keys.remove('keyblue')
        else:
            print('Stuck')  
            nextRoom(x, y) #backward
    except:
        print('Move to next room')
        nextRoom(x, y) #forward

def nextRoom(x, y):
    global WIDTH, HEIGHT, maps
    #forward
    if x >= WIDTH and maps.room == 0: #m1->m2
        maps.room += 1
        player.x = 0 * TILE_SIZE
    elif x >= WIDTH and maps.room == 1: #m2->m3
        maps.room += 1
        player.x = 0 * TILE_SIZE
    elif x >= WIDTH and maps.room == 3: #m4->m5
        maps.room += 1
        player.x = 0 * TILE_SIZE
    elif x >= WIDTH and maps.room == 4: #m5->m6
        maps.room += 1
        player.x = 0 * TILE_SIZE
    # if x >= WIDTH and maps.room in [0,1,3,4]: #m1->m2
    #     maps.room += 1
    #     player.x = 0 * TILE_SIZE

    #backward
    elif x < 0 and maps.room == 1: #m2->m1
        maps.room -= 1
        player.x = 7 * TILE_SIZE
    elif x < 0 and maps.room == 2: #m3->m2
        maps.room -= 1
        player.x = 7 * TILE_SIZE
    elif x < 0 and maps.room == 4: #m5->m4
        maps.room -= 1
        player.x = 7 * TILE_SIZE
    elif x < 0 and maps.room == 5: #m6->m5
        maps.room -= 1
        player.x = 7 * TILE_SIZE

    # downward
    elif y >= HEIGHT and maps.room == 0: #m1->m4
        maps.room += 3
        player.y = 0 * TILE_SIZE
    elif y >= HEIGHT and maps.room == 1: #m2->m5
        maps.room += 3
        player.y = 0 * TILE_SIZE
    elif y >= HEIGHT and maps.room == 2: #m3->m6
        maps.room += 3
        player.y = 0 * TILE_SIZE

    # upward
    elif y < 0 and maps.room == 3: #m4->m1
        maps.room -= 3
        player.y = 7 * TILE_SIZE
    elif y < 0 and maps.room == 4: #m5->m2
        maps.room -= 3
        player.y = 7 * TILE_SIZE
    elif y < 0 and maps.room == 5: #m6->m3
        maps.room -= 3
        player.y = 7 * TILE_SIZE

    print(f'Current Room : {maps.room+1}')

def update():
    pass

def draw():
    maps.generate()
    player.draw()
    enemy.draw()

pgzrun.go()