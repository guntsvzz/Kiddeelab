import pygame
import pgzrun
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600
#Class Actor
monkeyimage = ['monkey1','monkey2']
monkeySprite = Actor('monkey1') #object
#object.variables
monkeySprite.pos = (WIDTH/2,HEIGHT/2) #tuple #pos = position
#object.method()
import speech_recognition as sr
r = sr.Recognizer()

def draw():
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    monkeySprite.draw()

def moving(): #non-smoothing
    if monkeySprite.image == monkeyimage[0]: #check
        monkeySprite.image = monkeyimage[1] #change
    elif monkeySprite.image == monkeyimage[1]: #check
        monkeySprite.image = monkeyimage[0] #change

def monkey_limit():
    if monkeySprite.x >= WIDTH:
        monkeySprite.x = WIDTH
    if monkeySprite.x <= 0:
        monkeySprite.x = 0
    if monkeySprite.y >= HEIGHT:
        monkeySprite.y = HEIGHT
    if monkeySprite.y <= 0:
        monkeySprite.y = 0

def movement():
    if keyboard.w or keyboard.up: #full
        monkeySprite.y = monkeySprite.y - 5 #full
        moving()
    if keyboard.a or keyboard.left: #short
        monkeySprite.x -= 5 #short
        moving()
    if keyboard.s or keyboard.down: #short
        monkeySprite.y += 5 #short
        moving()    
    if keyboard.d or keyboard.right: #short
        monkeySprite.x += 5 #short
        moving()

def movement_speech(self,text):
        if self.text == 'ซ้าย':
            self.x -= self.speed #short
        if self.text == 'ขวา':
            self.x += self.speed #short

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
            
    movement_speech(text)
    movement()
    monkey_limit()

pgzrun.go()