import pgzrun
import random
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
TILE_SIZE = 70
WIDTH  = TILE_SIZE * number_column
HEIGHT = TILE_SIZE * number_row

class Map:
    def __init__(self, tile_size, num_row, num_column):
        self.tile_size = tile_size
        self.num_row =  num_row
        self.num_column = num_column

    def generate(self):
        for row in range(self.num_row):
            for column in range(self.num_column):
                x = column * self.tile_size 
                y = row * self.tile_size
                screen.blit('path', (x,y))
                material = maze[row][column]
                tile = tiles[material]
                if tile != 'path':
                    screen.blit(tile, (x,y))

map = Map(TILE_SIZE, number_row,number_column)

def draw():
    map.generate()

def update():
    pass

pgzrun.go()