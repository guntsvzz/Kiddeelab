import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (800,50)
import random
import pgzrun

#configuration
WIDTH, HEIGHT = 500, 800
TITLE = 'Space Invader'

class Player(Actor):
    def __init__(self,image_file):
        super().__init__(image_file)
        self.pos   = (WIDTH/2, HEIGHT-100)
        self.score = 0
        self.hp    = 3
        self.bullets = 10
        self.reload_time = 0.2 # 0.2 second reload time
        self.empty_bullet = False

    def shoot(self):
        if self.bullets > 0 and self.empty_bullet == False:
            return True
        else: 
            self.empty_bullet = True
            return False
 
    def reload(self, dt):
        if self.empty_bullet:
            print('reloading')
            self.reload_time -= dt
            if self.reload_time <= 0:
                self.bullets += 1
                if self.bullets > 10:
                    self.bullets = 10
                    self.empty_bullet = False
                    self.reload_time = 0
                    print('reload done')
                else:
                    self.reload_time = 0.2  # 0.2 second reload time

    def control(self):
        if keyboard.w or keyboard.UP:
            self.y -= 5
        if keyboard.a or keyboard.LEFT:
            self.x -= 5
        if keyboard.s or keyboard.DOWN:
            self.y += 5
        if keyboard.d or keyboard.RIGHT:
            self.x += 5
        #boundary
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT

class Bullet(Actor):
    def __init__(self,image_file):
        super().__init__(image_file)

bullets = []
player = Player('galaga')

def on_key_down(key):
    if key == key.SPACE and player.shoot():
        print('Shoot')
        bullets.append(Bullet('laserred'))
        bullets[-1].pos = player.pos
        player.bullets -= 1 

def draw_bullet():
    for b in bullets:
        b.draw()

def update_bullet():
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

def update(dt):
    player.control()
    player.reload(dt)
    update_bullet()

def draw():
    screen.blit('space_bg',(0,0))
    screen.draw.text(f'Score : {player.score}', pos = (10,20) , fontsize = 40)
    screen.draw.text(f'Bullets : {player.bullets}', pos = (340,20) , fontsize = 40)
    player.draw()
    draw_bullet()

pgzrun.go()