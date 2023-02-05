import pygame
import pgzrun
import random
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600


class Sprite(Actor):
    speed = 5 
    def __init__(self):
        super().__init__()
        self.WIDTH, self.HEIGHT = 800, 600
        self.pos = self.WIDTH/2,self.HEIGHT/2

    def movement(self):
        if keyboard.w or keyboard.up: #full
            self.y -= self.speed #full
            # moving()
        if keyboard.a or keyboard.left: #short
            self.x -= self.speed #short
            # moving()
        if keyboard.s or keyboard.down: #short
            self.y += self.speed #short
            # moving()    
        if keyboard.d or keyboard.right: #short
            self.x += self.speed #short
            # moving()

    def monkey_limit(self):
        if self.x >= WIDTH:
            self.x = WIDTH
        if self.x <= 0:
            self.x = 0
        if self.y >= HEIGHT:
            self.y = HEIGHT
        if self.y <= 0:
            self.y = 0

monkey = Sprite('monkey1')
monkey.pos = (WIDTH/2,HEIGHT/2)

def draw():
    screen.clear()
    monkey.draw()

def update(): #1/60 second
    monkey.movement()

pgzrun.go()