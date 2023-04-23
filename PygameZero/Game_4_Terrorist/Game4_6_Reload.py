import pygame 
import pgzrun
import random

TITLE = 'Game 4 Terrorist'
WIDTH, HEIGHT = 800, 600
class Bullet(Actor):
    def __init__(self, image_file, center = (650, 40)):
        super().__init__(image_file, center)
        self.center = center
        
class Person(Actor):
    def __init__(self, image_file, hostage = False, pos = (random.randint(10,790), 550)):
        super().__init__(image_file, pos)
        self.pos = pos
        self.hostage = hostage
        self.rise = [0.5, 1, 1.5, 2, 2.5] #List to random
        self.out  = [0.5, 1, 1.5, 2, 2.5]
        self.timerise = self.rise[random.randint(0,4)]
        self.timeout  = self.out[random.randint(0,4)]

    def moving(self):
        self.timerise -= 1/60 #60 fps
        if self.timerise <= 0:
            self.y -= 3
            if self.y < 350:
                self.y = 350
                self.timeout -= 1/60
                if self.timeout <= 0:
                    self.y = 550
                    self.x = random.randint(10,790)
                    self.timerise = self.rise[random.randint(0,4)]
                    self.timeout = self.out[random.randint(0,4)]

class Gun(Actor):
    def __init__(self, image_file):
        super().__init__(image_file)
        self.game_state = 'main'
        self.score = 0
        self.amount = 6
        self.magazines = 1
        self.reload_timer = 3
        self.is_reloading = False

    def gameSong(self):
        if self.game_state == 'win' :
            sounds.win.play()
            sounds.snarebeat.stop()
        elif self.game_state == 'gameover' :
            sounds.gameover.play()
            sounds.snarebeat.stop()
        elif self.game_state == 'play' :
            sounds.snarebeat.play(-1)
            sounds.gameover.stop()
            sounds.win.stop()    

    def checking_bullet(self):
        if self.is_reloading:
            while self.amount <= 5:
                self.reload_timer -= 1/60
                bullets.append(Bullet('bullet', center=(650 + self.amount*25, 40)))
                self.amount += 1
            self.is_reloading = False

hostage_Sprite = Person('hostage', hostage=True)
terror1_Sprite = Person('terror1')
terror2_Sprite = Person('terror2')

gun_center = Gun('crosshair')

bullets = []
for idx in range(gun_center.amount):
    bullets.append(
        Bullet('bullet', center=(650+idx*25, 40))
    )  

def on_mouse_down(pos, button): 
    print(gun_center.amount)
    if len(bullets) > 0:
        bullets.pop()
        gun_center.amount -= 1
    else:
        gun_center.is_reloading = True

    if button == mouse.LEFT :
        #####hostage shot
        if hostage_Sprite.collidepoint(pos) :
            hostageshot = True
            print('Hostage shot')
            gun_center.game_state = 'gameover'
            gun_center.gameSong()
        else :
            hostageshot = False
        ####terror1 shot
        if terror1_Sprite.collidepoint(pos) :
            terror1shot = True
            print('Terror1 shot')
            gun_center.score += 1
            terror1_Sprite.pos =(random.randint(10, 790), 550) 
        else :
            terror1shot = False
        ####terror2 shot
        if terror2_Sprite.collidepoint(pos) :
            terror2shot = True
            print('Terror2 shot')
            gun_center.score += 2
            terror2_Sprite.pos =(random.randint(10, 790), 550) 
        else :
            terror2shot = False
        ####State
        if gun_center.score > 10:
            gun_center.game_state = 'win'
            gun_center.gameSong()

def on_mouse_move(pos, rel, buttons):
    gun_center.x = pos[0]
    gun_center.y = pos[1]

def update():
    if gun_center.game_state == 'play' : 
        hostage_Sprite.moving()
        terror1_Sprite.moving()
        terror2_Sprite.moving()
        gun_center.checking_bullet()
    
def draw():
    screen.blit('background',(0,0))
    def restart() :
        screen.draw.text('Restart' , center=(400, 300), color=(255, 0, 0), fontsize=80)
        screen.draw.text('Press space bar to play' , center=(400, 350), color=(255, 0, 0), fontsize=50)
        if keyboard.space == True :
            gun_center.game_state = 'play'
            gun_center.score = 0
            hostage_Sprite.pos =(random.randint(10, 790), 550) 
            terror1_Sprite.pos =(random.randint(10, 790), 550) 
            terror2_Sprite.pos =(random.randint(10, 790), 550) 
            gun_center.gameSong()

    if gun_center.game_state == 'main' : #Main Screen
        screen.draw.text('Save Hostage' , center=(400, 200), color=(255, 255, 255), fontsize=100)
        restart()
    elif gun_center.game_state == 'gameover' : 
        screen.draw.text('Game Over' , center=(400, 200), color=(255, 255, 255), fontsize=100)
        restart()
    elif gun_center.game_state == 'win' : 
        screen.draw.text('You Win' , center=(400, 200), color=(255, 255, 255), fontsize=100)
        restart()
    elif gun_center.game_state == 'play' :  
        screen.draw.text(f'Score : {gun_center.score}',(15,20),color=(255,255,255),fontsize=40)
        hostage_Sprite.draw()
        terror1_Sprite.draw()
        terror2_Sprite.draw()
        gun_center.draw()

        for b in bullets:
            b.draw()

    screen.blit('wall',(0,400)) #x, y shift 400 unit

pgzrun.go()
