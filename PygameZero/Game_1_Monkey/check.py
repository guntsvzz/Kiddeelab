import pgzrun
import pygame

TITLE = 'Game'
WIDTH, HEIGHT = 800,600

# monkey = Actor('monkey1', pos = (WIDTH/2, HEIGHT/2)) #img,pos

class Actor:
    def __init__(self, img, pos):
        self.img = img
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
    
    def draw():
        pass

class Monkey(Actor):
    def __init__(self, img, pos):
        super().__init__(img, pos)
        pass

monkey = Monkey('monkey1', pos = (WIDTH/2, HEIGHT/2)) #img,pos  

def move():
    if keyboard.w == True:
        monkey.y -= 1 
    if keyboard.s:
        monkey.y += 1
    if keyboard.a:
        monkey.x -= 1
    if keyboard.d:
        monkey.x += 1

def update():
    move()

def draw():
    monkey.draw()

pgzrun.go()