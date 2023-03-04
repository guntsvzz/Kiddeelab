import pgzrun
import random
tiles = {
    0 : 'path', 
    1 : 'wall', 
    2 : 'lock_yellow',
    3 : 'close_door',
    4 : 'key_yellow'
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
enemy = Actor("blockermad", anchor=(-10, -10), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))
enemy.yv = -1
enemy.xv = -1

def draw():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            screen.blit('path', (x, y))

            tile = tiles[maze[row][column]]
            if tile != 'path':
                screen.blit(tile, (x, y))

    grassblock.draw()
    enemy.draw()

def on_key_down(key):
    global unlock
    #Moving Part
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

    #if tile is path, player can move
    if tile == 'path':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        print('x:{} y:{}'.format(x, y))
        animate(grassblock, duration=0.1, pos=(x, y))
    #if tile is unlock, game stop
    elif tile == 'lock_yellow':
        print("Well done")
        exit()
    #if tile get key, unlock = 1
    elif tile == 'key_yellow':
        unlock = unlock + 1
        maze[row][column] = 0 #path
    elif tile == 'close_door' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0 #path

    enemyMoving()

def enemyMoving():
    # enemy movement
    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)

    row = row + enemy.yv
    column = column + enemy.xv

    tile = tiles[maze[row][column]]
    if not tile == 'wall':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration=0.1, pos=(x, y))
    else:
        rd = random.randint(1,2)
        if rd == 1:
            enemy.yv = enemy.yv * -1
        elif rd == 2:
            enemy.xv = enemy.xv * -1

    if enemy.colliderect(grassblock):
        print("You died")
        exit()

def update():
    pass

pgzrun.go()