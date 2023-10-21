import pygame
import pgzrun
import random
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600

import speech_recognition as sr
r = sr.Recognizer()

class Sprite(Actor):
    speed = 5 
    def __init__(self):
        super().__init__()
        self.WIDTH, self.HEIGHT = 800, 600
        self.pos = self.WIDTH/2,self.HEIGHT/2

    def movement_keyboard(self):
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
            
    def movement_speech(self,text):
        if self.text == 'ซ้าย':
            self.x -= self.speed #short
        if self.text == 'ขวา':
            self.x += self.speed #short

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
    
    with sr.Microphone() as source:
        print('Start Speaking now')
        # while True:
        audio = r.listen(source)
        text = r.recognize_google(audio,language = "th-TH")
        try:
            print("You said " + text) # แสดงข้อความจากเสียงด้วย Google Speech Recognition และกำหนดค่าภาษาเป็นภาษาไทย
        except sr.RequestError as e: # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
            print("Could not understand audio")
        monkey.movement_speech(text)

pgzrun.go()
