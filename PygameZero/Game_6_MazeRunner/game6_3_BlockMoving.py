import pgzrun
import random

TILE = {
    0 : 'path',
    1 : 'wall'
}
# print(tiles[0],tiles[1])
# MAZE = [A, B, C, D, E, F]
MAZE = [
    #0 1 2 3 4 5 6 7
    [1,1,1,1,1,1,1,1], #0
    [1,0,0,0,1,1,0,1], #1
    [1,0,1,0,0,0,0,1], #2
    [1,0,0,1,0,0,0,1], #3
    [1,1,0,1,1,1,0,1], #4
    [0,0,0,0,1,1,0,0], #5
    [0,0,1,1,0,1,0,0], #6
    [1,0,1,0,0,0,0,1], #7
] #8 rows, 6 columns
number_column = len(MAZE[0]) #changable
number_row = len(MAZE) #changable

TILE_SIZE = 70
WIDTH = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row

#class : map, player, enemy
class Map: #screen.blit
    def __init__(self, tile_size, num_row, num_column, maze, tile):
        self.tile_size = tile_size
        self.num_row = num_row
        self.num_column = num_column
        self.maze = maze
        self.tile = tile

    def generate(self): #generating a map 
        for row in range(self.num_row): 
            for column in range(self.num_column):
                #drawing path
                # print(row, column)
                x = self.tile_size * column
                y = self.tile_size * row
                screen.blit('path',(x,y))
                #drawing walls
                material = self.maze[row][column]
                t = self.tile[material]
                if t == 'wall':
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

maps = Map(TILE_SIZE, number_row, number_column, MAZE, TILE)
player = Player('grassblock')
enemy = Enemy('blockermad')

def on_key_down(key): #for toggle keyboard
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
        print(row, column)
        material = MAZE[row][column]
        if (TILE[material] == 'path') and (0 <= row <= number_row) and (0 <= column <= number_column):
            animate(player, duration = 0.1, pos = (x,y))
        else:
            print('Stuck')
    except:
        pass

def update():
    pass

def draw():
    maps.generate()
    player.draw()
    enemy.draw()

pgzrun.go()