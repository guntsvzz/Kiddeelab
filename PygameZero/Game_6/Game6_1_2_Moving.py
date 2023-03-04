import pgzrun
tiles = {
    0 : 'castlecenter', 
    1 : 'boxalt', 
    2 : 'lock_yellow',
    3 : 'door_closedmid',
    4 : 'keyyellow'
}

unlock = 0
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 3, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 4, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

width,height = len(maze[0]),len(maze)
TILE_SIZE = 70 #pixel of image
WIDTH = TILE_SIZE * width
HEIGHT = TILE_SIZE * height

grassblock = Actor("grassblock", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
blockermad = Actor("blockermad", anchor=(-10, -10), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))

def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
    grassblock.draw()
    blockermad.draw()

def on_key_down(key):
    row = int(grassblock.y / TILE_SIZE)
    column = int(grassblock.x / TILE_SIZE)
    if key == key.UP or key == key.W:
        row -= 1
    if key == key.DOWN or key == key.S:
        row += 1
    if key == key.LEFT or key == key.A:
        column -= 1
    if key == key.RIGHT or key == key.D:
        column += 1
    tile = tiles[maze[row][column]]
    if tile == 'castlecenter':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        print('x:{} y:{}'.format(x, y))
        animate(grassblock, duration=0.1, pos=(x, y))
    elif tile == 'lock_yellow':
        print("Well done")

def update():
    pass

pgzrun.go()