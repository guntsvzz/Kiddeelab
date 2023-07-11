import pgzrun
import random
import maths

TITLE = 'Shoot some racist guys'
WIDTH, HEIGHT = 800, 600

#Define the button properties
BUTTON_WIDTH = 200
BUTTON_HEIGHT  = 80
BUTTON_X = WIDTH // 2 - BUTTON_WIDTH // 2
BUTTON_Y1 = HEIGHT // 2 - 100 
BUTTON_Y2 = HEIGHT // 2 + 50
BUTTON_Y3 = HEIGHT // 2 + 200

def button_click(button_pressed):
    pass #next week 

button_pressed = 0

def on_key_down(key):
    global button_pressed
    if key == keys.UP:
        button_pressed -= 1
        if button_pressed < 0:
            button_pressed = 0
    elif key == keys.DOWN:
        button_pressed +=1 
        if button_pressed > 2:
            button_pressed = 2
    elif key == keys.SPACE:
        button_click(button_pressed)
    print(button_pressed)

def update():
    pass

def draw():
    screen.blit('background.png',(0,0))
    screen.blit('wall.png',(0, 400))
    screen.draw.text('Shoot some racist guys', center = (WIDTH/2, HEIGHT/2 - 150), fontsize = 100)

    #button1
    if button_pressed == 0:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y1),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Start', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y1 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    #button2
    if button_pressed == 1:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y2),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Options', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y2 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)
    #button3
    if button_pressed == 2:
        screen.draw.filled_rect(Rect((BUTTON_X, BUTTON_Y3),(BUTTON_WIDTH, BUTTON_HEIGHT)), 'white') #filled_rect( Rect((x,y),(w,h)) , color )
        screen.draw.text('Exit', center = (BUTTON_X + BUTTON_WIDTH/2, BUTTON_Y3 + BUTTON_HEIGHT/2), color = 'black', fontsize = 60)

pgzrun.go()