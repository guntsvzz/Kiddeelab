import pygame 
import pgzrun
import random

TITLE = 'Game 4 Terrorist'
WIDTH, HEIGHT = 800, 600

class Person(Actor):
    def __init__(self, image_file, hostage = False, pos = (random.randint(10,790), 550)):
        super().__init__(image_file, pos)
        self.pos = pos
        self.hostage = hostage
        self.rise = [0.5, 1, 1.5, 2, 2.5] #List to random
        self.out  = [0.5, 1, 1.5, 2, 2.5]
        self.timerise = self.rise[random.randint(0,4)]
        self.timeout  = self.out[random.randint(0,4)]

    def score(self):
        if self.hostage: #Lose
            pass
        else: #get score
            pass

    def moving(self):
        self.timerise -= 1/60 #60 fps
        if self.timerise <= 0:
            self.y -= 2
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

hostage_Sprite = Person('hostage', hostage=True)
terror1_Sprite = Person('terror1')
terror2_Sprite = Person('terror2')

gun_center = Gun('crosshair')

def on_mouse_move(pos, rel, buttons):
    gun_center.x = pos[0]
    gun_center.y = pos[1]

def on_mouse_down(pos, button):
    if button == mouse.LEFT :
        #hostage shot
        if hostage_Sprite.collidepoint(pos) :
            hostageshot = True
            print('Hostage shot')
        else :
            hostageshot = False
        #terror1 shot
        if terror1_Sprite.collidepoint(pos) :
            terror1shot = True
            print('Terror1 shot')
            gun_center.score += 1
            terror1_Sprite.pos =(random.randint(10, 790), 550) 
        else :
            terror1shot = False
        #terror2 shot
        if terror2_Sprite.collidepoint(pos) :
            terror2shot = True
            print('Terror2 shot')
            gun_center.score += 2
            terror2_Sprite.pos =(random.randint(10, 790), 550) 
        else :
            terror2shot = False
        if gun_center.score > 5:
            gun_center.game_state = 'win'
    
def update():
    hostage_Sprite.moving()
    terror1_Sprite.moving()
    terror2_Sprite.moving()

def draw():
    screen.blit('background',(0,0))
    hostage_Sprite.draw()
    terror1_Sprite.draw()
    terror2_Sprite.draw()
    screen.blit('wall',(0,400)) #x, y shift 400 unit
    gun_center.draw()

pgzrun.go()
