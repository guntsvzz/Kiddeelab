import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (200,50)
import pgzrun, pygame, random

#resolution is in pixels
WIDTH, HEIGHT = 500, 800
TITLE = 'Space Invader'

bullets =[]

class Player(Actor):
    #properties/ variable
    def __init__(self, image_file, pos):
        super().__init__(image_file, pos)
        self.score = 0
        self.game_state = 'main'
        
    #function/ method
    def keybutton(self):
        #setting moving
        if keyboard.w:
            self.y -= 5
        if keyboard.s:
            self.y += 5
        if keyboard.a:
            self.x -= 5
        if keyboard.d:
            self.x += 5
    
        #setting boundary
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

class Bullet(Actor):
    #properties/ variable
    def __init__(self, image_file):
        super().__init__(image_file)
        self.is_reloading = False
        self.amount = 10

class Enemy(Actor):
    #properties/ variable
    def __init__(self, image_file):
        super().__init__(image_file)

bugXdirection = 1
bugMoveDown = False

player = Player('galaga', pos = (WIDTH/2, 550))

enemies = []
def createEnemy():
    for row in range(0,3,1):
        for column in range(0,6,1):
            enemies.append(Enemy('bug'))
            enemies[-1].x = 10 + 80*column #[-1] refer to the last item
            enemies[-1].y = 50 + 60*row

# createEnemy() #calling to create 10 bugs

def on_key_down(key):
    if key == key.SPACE:
        bullets.append(Bullet('laserred'))
        bullets[-1].pos = player.pos

def drawbullets():
    for bullet in bullets: 
        bullet.draw()

def drawenemies():      
    for enemy in enemies:
        enemy.draw()

def updatedBullets():
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet) #specific value
        else:
            bullet.y -= 10

    #collision enemy
        for enemy in enemies:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy) 
                player.score += 1
                
def updatedEnemies():
    global bugMoveDown, bugXdirection
    try:
        if enemies[-1].x > WIDTH or enemies[0].x < 0:
            bugMoveDown = True
            bugXdirection *= -1
    except:
        player.game_state = 'win'

    for enemy in enemies:
        enemy.x += 1 * bugXdirection
        if bugMoveDown == True:
            enemy.y += 5
    bugMoveDown = False

def restart():
    screen.draw.text('Restart' , center=(WIDTH/2, HEIGHT/2+50), color=(255, 0, 0), fontsize=40)
    screen.draw.text('Press space bar to play' , center=(WIDTH/2, HEIGHT/2+100), color=(255, 0, 0), fontsize=30)
    if keyboard.space == True :
        player.game_state = 'play'
        player.score = 0
        createEnemy()

def draw():
    # screen.blit('galagabg', (0,0))
    screen.clear()
    if player.game_state == 'main' : #Main Screen
        screen.draw.text('Space Invader' , center=(WIDTH/2, HEIGHT/2), color=(255, 255, 255), fontsize=80)
        restart()
    elif player.game_state == 'lose' : 
        screen.draw.text('Game Over' , center=(WIDTH/2, HEIGHT/2), color=(255, 255, 255), fontsize=80)
        restart()
    elif player.game_state == 'win': 
        screen.draw.text('You Win' , center=(WIDTH/2, HEIGHT/2), color=(255, 255, 255), fontsize=80)
        restart()
    elif player.game_state == 'play' :   
        screen.draw.text(f'Score : {player.score}',(15,20),color=(255,255,255),fontsize=40)
        player.draw()
        drawbullets()
        drawenemies()

def update():
    player.keybutton()
    updatedBullets()
    updatedEnemies()

pgzrun.go()