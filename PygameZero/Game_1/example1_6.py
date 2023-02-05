import pygame
import pgzrun
import random
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600

#Class Actor
monkeyimage = ['monkey1','monkey2']
#object = class()
monkeySprite = Actor('monkey1') #object
#object.variables
monkeySprite.pos = (WIDTH/2,HEIGHT/2) #tuple #pos = position
#object.method()
bananaSprite = Actor('banana')
bananaSprite.pos = (random.randint(0,WIDTH),0)
spiderSprite = Actor('spider')
spiderSprite.pos = (random.randint(0,WIDTH),0)

monkeySprite.score = 0
monkeySprite.hp = 5

#game state
game_state = 'play'

def draw():
    global game_state
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    if game_state == 'win':
        screen.draw.text(f'WIN\nScore : {monkeySprite.score}',center = (WIDTH/2,HEIGHT/2), color=(255,255,255),fontsize=40)
    elif game_state == 'lose':
        screen.draw.text(f'LOSE\nScore : {monkeySprite.score}',center = (WIDTH/2,HEIGHT/2), color=(255,255,255),fontsize=40)
    else:     
        monkeySprite.draw()
        bananaSprite.draw()
        spiderSprite.draw()
        #Format:  screen.draw.text(text, (x,y), color=(r,g,b), fontsize=20)
        screen.draw.text(f'Score : {monkeySprite.score}',(15,10),color=(255,255,255),fontsize=40)
        screen.draw.text(f'HP : {monkeySprite.hp}',(15,50),color=(255,255,255),fontsize=40)

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

def movement(speed = 5):
    if keyboard.w or keyboard.up: #full
        monkeySprite.y = monkeySprite.y - speed #full
        moving()
    if keyboard.a or keyboard.left: #short
        monkeySprite.x -= speed #short
        moving()
    if keyboard.s or keyboard.down: #short
        monkeySprite.y += speed #short
        moving()    
    if keyboard.d or keyboard.right: #short
        monkeySprite.x += speed #short
        moving()

def bananaSpawn(speed = 6):
    bananaSprite.y += speed
    if bananaSprite.y > HEIGHT:
        bananaSprite.x = random.randint(0,WIDTH)
        bananaSprite.y = 0
   
def spiderSpawn(speed = 6):
    spiderSprite.y += speed
    if spiderSprite.y > HEIGHT:
        spiderSprite.pos = (random.randint(0,WIDTH),0)
   
def spiderHitMonkey():
    if spiderSprite.colliderect(monkeySprite):
        monkeySprite.hp -= 1 #monkeySprite.hp = monkeySprite.hp - 1
        spiderSprite.pos = (random.randint(0,WIDTH), 0) #(x,y) #random.randint(start,stop)

def bananaHitMonkey():
    if bananaSprite.colliderect(monkeySprite):
        monkeySprite.score += 1
        bananaSprite.pos = (random.randint(0,WIDTH),0)

def gamesound():
    global game_state
    if game_state == 'win':
        sounds.win.play()  
    elif game_state == 'lose':
        sounds.lose.play()  
    else: 
        sounds.jungle.play(-1)

def result():
    global game_state
    if monkeySprite.hp < 1:
        game_state = 'lose'
        gamesound()
    if monkeySprite.score > 9:
        game_state = 'win'
        gamesound()

def update(): #1/60 second
    movement(8)
    monkey_limit()
    bananaSpawn()
    spiderSpawn()
    spiderHitMonkey()
    bananaHitMonkey()
    result()

gamesound()
pgzrun.go()