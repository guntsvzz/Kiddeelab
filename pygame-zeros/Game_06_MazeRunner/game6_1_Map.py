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
    [1,0,0,0,1,1,0,1], #5
    [1,0,1,1,0,1,0,1], #6
    [1,0,1,0,0,0,0,1], #7
] #8 rows, 6 columns

number_column = len(MAZE[0]) #changable
number_row = len(MAZE) #changable

TILE_SIZE = 70
WIDTH = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row

#class : map, player, enemy
class Map: #screen.blit
    def __init__(self, tile_size, num_row, num_column, maze,tile):
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

maps = Map(TILE_SIZE, number_row, number_column, MAZE, TILE)

def update():
    pass

def draw():
    maps.generate()

pgzrun.go()