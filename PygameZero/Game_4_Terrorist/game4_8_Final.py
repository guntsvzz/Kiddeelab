import pgzrun
import random
import math
import pygame

TITLE = 'Shoot some racist guys'
WIDTH, HEIGHT = 800, 600

#Define the button properties
BUTTON_WIDTH = 200
BUTTON_HEIGHT  = 80
BUTTON_X = WIDTH // 2 - BUTTON_WIDTH // 2
BUTTON_Y1 = HEIGHT // 2 - 100 
BUTTON_Y2 = HEIGHT // 2 + 50
BUTTON_Y3 = HEIGHT // 2 + 200

###########
# Sprite
###########
class Bullet(Actor):
    def __init__(self, image_file, center = (650,40)):
        super().__init__(image_file, center)
        self.center = center

class NPC(Actor):
    def __init__(self, image_file, hostage = True):
        super().__init__(image_file) 
        self.pos = (random.randint(0,WIDTH), HEIGHT)
        self.time = [2, 3, 4, 5]
        self.waiting = 1
        self.moving = 'up'

    def move(self):
        self.waiting = -1/60
        if self.moving == 'up':
            if self.waiting <= 0:
                self.y -= 3 #move up
                if self.y < 350: #set the limit
                    self.y = 350
                    self.waiting = self.time[random.randrange(0,len(self.time))] 
                    self.moving = 'down'

        elif self.moving == 'down':
            if self.waiting <= 0:
                self.y += 3
                if self.y > 550:
                    self.y = 550
                    self.x = random.randint(0, WIDTH)
                    self.waiting = self.time[random.randrange(0,len(self.time))]
                    self.moving = 'up'

class Gun(Actor):
    def __init__(self, image_file):
        super().__init__(image_file)
        self.game_state = "main"
        self.score = 0
        self.amount = 6
        self.is_reloading = False
        self.reload_time = 1

    def reload(self, dt): #next week;
        if self.is_reloading == True :
            while self.amount <= 5:
                self.reload_time -= dt
                if self.reload_time <= 0:
                    bullets.append(
                        Bullet('bullet', center = (650+self.amount*25,40))
                    )
                    self.amount += 1
                    print(f'Reloading : {self.amount}')
                    self.reload_time = 1
            self.is_reloading = False

hostage = NPC('hostage', hostage = True)
terror1 = NPC('terror1')
terror2 = NPC('terror2')
gun_center = Gun('crosshair')


def addbullets(bullets = []):
    for idx in range(gun_center.amount):
        bullets.append(
            Bullet('bullet', center = (650+idx*25,40))
        )
    return bullets

bullets = addbullets()

def on_mouse_move(pos, rel, buttons):
    gun_center.x = pos[0]
    gun_center.y = pos[1]

###########
# GUI
###########
def button_click(button_pressed):
    if button_pressed == 0:
        gun_center.game_state = 'play'
    elif button_pressed == 1:
        pass #options
    elif button_pressed == 2:
        pgzrun.quit()
    elif button_pressed == 3:
        gun_center.game_state = 'main'

button_pressed = 0

def on_key_down(key):
    global button_pressed
    if gun_center.game_state == 'main':
        if key == keys.UP:
            button_pressed -= 1
            if button_pressed < 0:
                button_pressed = 0
        elif key == keys.DOWN:
            button_pressed +=1 
            if button_pressed > 2:
                button_pressed = 2
        elif key == keys.RETURN:
            print('ENTER')
            button_click(button_pressed)

    if gun_center.game_state in ['win','lose']: #gun_center.game_state == 'win' or gun_center.game_state == 'lose'
        if key == keys.UP:
            button_pressed = 0 
        elif key == keys.DOWN:
            button_pressed = 3
        elif key == keys.RETURN:
            print('ENTER')
            button_click(button_pressed)
            button_pressed = 0 #default 
        print(button_pressed)

def on_mouse_down(pos,button):
    #checking bullet and magazine
    if gun_center.amount > 1 and gun_center.game_state == 'play':
        bullets.pop() #delete last item inside list
        gun_center.amount -= 1
        print(f'Remain : {gun_center.amount}')
    else:
        gun_center.is_reloading = True

    if gun_center.is_reloading == False:
        #click to shoot
        if button == mouse.LEFT:
            if hostage.collidepoint(pos):
                gun_center.game_state = 'lose'
            if terror1.collidepoint(pos):
                gun_center.score += 1
                terror1.pos = (random.randint(0,WIDTH),HEIGHT)
            if terror2.collidepoint(pos):
                gun_center.score += 1
                terror2.pos = (random.randint(0,WIDTH),HEIGHT)
    #condition to win
    if gun_center.score >= 10 :
        gun_center.game_state = 'win'

###########
# Main Update
###########
def update(dt):
    if gun_center.game_state == 'play':
        terror1.move()
        terror2.move()
        hostage.move()
        gun_center.reload(dt)

def draw():
    screen.blit('background.png',(0,0))
    screen.blit('wall.png',(0, 400))
    def restart():
        global bullets
        #restart score and position of hostage & terrorists
        gun_center.score = 0
        gun_center.amount = 6
        hostage.pos = (random.randint(0,WIDTH),HEIGHT) 
        terror1.pos = (random.randint(0,WIDTH),HEIGHT)
        terror2.pos = (random.randint(0,WIDTH),HEIGHT)
        bullets.clear() #delete item inside the list
        bullets = addbullets()
        
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
        

    if gun_center.game_state == 'main':
        screen.draw.text('Shoot some racist guys', center = (WIDTH/2, HEIGHT/2 - 150), fontsize = 100)
        #button1
        if button_pressed == 0:
            screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y1),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
            screen.draw.text('Start', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y1 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
        else:
            screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y1),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
            screen.draw.text('Start', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y1 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
        #button2
        if button_pressed == 1:
            screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
            screen.draw.text('Options', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
        else:
            screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
            screen.draw.text('Options', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
        #button3
        if button_pressed == 2:
            screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y3),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
            screen.draw.text('Exit', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y3 + BUTTON_HEIGHT/2), color = 'red', fontsize = 60)
        else:
            screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y3),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
            screen.draw.text('Exit', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y3 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    elif gun_center.game_state == 'win':
        screen.draw.text('You WIN',center = (WIDTH/2, HEIGHT/2-100), fontsize = 100)
        restart()
    elif gun_center.game_state == 'lose':
        screen.draw.text('You LOSE',center = (WIDTH/2, HEIGHT/2-100), fontsize = 100)
        restart()
    elif gun_center.game_state == 'play':
        screen.draw.text(f'Score : {gun_center.score}', pos = (10,20) , fontsize = 40)
        terror1.draw()
        terror2.draw()
        hostage.draw()
        screen.blit('wall.png',(0,400))
        gun_center.draw()

        for b in bullets:
            b.draw()
     
pgzrun.go()