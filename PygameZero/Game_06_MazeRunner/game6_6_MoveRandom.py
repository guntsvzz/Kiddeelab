import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (500, 200) #x,y
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
    9 : 'lock_blue',
    -99 : 'nothing'

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
TITLE = 'random game with grass box'

#Define the button properties
BUTTON_WIDTH = 200
BUTTON_HEIGHT  = 80
BUTTON_X = WIDTH // 2 - BUTTON_WIDTH // 2
BUTTON_Y1 = HEIGHT // 2 - 100 
BUTTON_Y2 = HEIGHT // 2 + 50
BUTTON_Y3 = HEIGHT // 2 + 200

#This is the actual timer 
timer_start = 0
timer = timer_start

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
        self.game_state = 'main'

class Enemy(Actor):
    def __init__(self, image_file, room, anchor = (-10,-10)):
        super().__init__(image_file, anchor)
        self.anchor = anchor
        self.room = room
        self.main = MAIN
        self.p1, self.p2 = self.random_spawn()
        self.pos = (self.p1*TILE_SIZE,self.p2*TILE_SIZE)

    def random_spawn(self):
        rooms = self.main[self.room]
        coordinates = []
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == 0:
                    coordinates.append((x,y))

        return random.choice(coordinates) #(x,y)
    
    def collision(self):
        if self.colliderect(player):
            player.game_state = 'lose'

    def move(self):
        if player.game_state == 'play':
            row = int(self.y/TILE_SIZE) #0,1,2,3,4,5,6,7
            column = int(self.x/TILE_SIZE) #1,2,3,4,5,6,7
        
            steps = [(-1,0), (1,0), (0,1), (0,-1)] #column, row 
                    #left   #right #down  #up
            diff_x, diff_y  = random.choice(steps) #select random x,y

            try :
                material = self.main[self.room][row+diff_x][column+diff_y] #check next material
            except:
                material = -99

            if TILE[material] == 'path' \
                and (0 <= row+diff_x <= number_row) \
                and (0 <= column+diff_y <= number_column):

                row += diff_x
                column +=diff_y
                self.pos = (column * TILE_SIZE, row * TILE_SIZE)


maps = Map(TILE_SIZE, number_row, number_column, MAIN, TILE)
player = Player('grassblock')

enemy1 = Enemy('blockermad', room = 0)
enemy2 = Enemy('blockermad', room = 1)
enemy3 = Enemy('blockermad', room = 2)
enemy4 = Enemy('blockermad', room = 3)
enemy5 = Enemy('blockermad', room = 4)
enemy6 = Enemy('blockermad', room = 5)
enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6]
keys = []

def button_click(button_pressed):
    if button_pressed == 0:
        player.game_state = 'play' #restart or play
        # for en in enemies:
        #     en.random_spawn()
    elif button_pressed == 1:
        pass #options
    elif button_pressed == 2: #quit the game
        pgzrun.quit()
    elif button_pressed == 3:
        player.game_state = 'main' #main menu

button_pressed = 0

def on_key_down(key): #for toggle keyboard
    global MAIN, keys, maps, button_pressed
    if player.game_state == 'play':
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

    elif player.game_state == 'main':
        if key == key.UP:
            button_pressed -= 2
            if button_pressed < 0:
                button_pressed = 0
        elif key == key.DOWN:
            button_pressed += 2
            if button_pressed > 2:
                button_pressed = 2
        elif key == key.RETURN:
            print('enter main')
            button_click(button_pressed)

    elif player.game_state in ['win','lose']:
        if key == key.UP:
            button_pressed = 0 #main menu
        elif key == key.DOWN:
            button_pressed = 3 #restart the game
        elif key == key.RETURN:
            print('enter win lose')
            button_click(button_pressed)
            button_pressed = 0 #seting as default again

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

def update(time_interval): #with in 1 sec it run 60 times  = 1/60
    global timer, enemies
    # enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6]
    if player.game_state == 'play':
        timer += time_interval #Count up
        if timer >= 0.5:
            for en in enemies:
                en.move()
            # enemy1.move()
            # enemy2.move()
            # enemy3.move()
            # enemy4.move()
            # enemy5.move()
            # enemy6.move()
            timer = 0

        for en in enemies:
            en.collision()
    

def restart(): #win,lose
    keys.clear() #remove all keys
    #button1
    if button_pressed == 0:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Restart', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
    else:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Restart', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    #button2
    if button_pressed == 3:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y3),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Main', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y3 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
    else:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y3),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Main', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y3 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    

def main(): #main
    #button1
    if button_pressed == 0:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y1),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Start', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y1 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
    else:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y1),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Start', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y1 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    #button2
    if button_pressed == 2:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Exit', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
    else:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Exit', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    

def draw():
    maps.generate()
    if player.game_state == 'main':
        screen.draw.text('Random Game with\nThe grass box',center = (WIDTH/2, HEIGHT/2-150), fontsize = 80)
        main()
    elif player.game_state == 'win':
        screen.draw.text('You WIN',center = (WIDTH/2, HEIGHT/2-100), fontsize = 80)
        restart()
    elif player.game_state == 'lose':
        screen.draw.text('You LOSE',center = (WIDTH/2, HEIGHT/2-100), fontsize = 80)
        restart()
    elif player.game_state == 'play':
        player.draw()
        if maps.room == 0 : #it should spawn in room 0
            enemy1.draw()
        elif maps.room == 1: #it should spawn in room 1
            enemy2.draw()
        elif maps.room == 2: #it should spawn in room w
            enemy3.draw()
        elif maps.room == 3: #it should spawn in room w
            enemy4.draw()
        elif maps.room == 4: #it should spawn in room w
            enemy5.draw()
        elif maps.room == 5: #it should spawn in room w
            enemy6.draw()


pgzrun.go()