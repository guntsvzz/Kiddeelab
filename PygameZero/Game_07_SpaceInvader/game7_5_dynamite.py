import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (800,50)
import random
import pgzrun

#configuration
WIDTH, HEIGHT = 500, 800
TITLE = 'Space Invader'

class Enemy(Actor):
    def __init__(self,image_file, pos):
        super().__init__(image_file, pos)

class Player(Actor):
    def __init__(self,image_file):
        super().__init__(image_file)
        self.pos   = (WIDTH/2, HEIGHT-100)
        self.score = 0
        self.hp    = 3
        self.bullets = 10
        self.reload_time = 0.2 # 0.2 second reload time
        self.empty_bullet = False
        self.game_state = 'main'
        self.level = 1

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
                    sounds.bullet_reload.play()

    def control(self):
        if self.game_state == 'play':
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

class Dynamite(Actor):
    def __init__(self,image_file):
        super().__init__(image_file)

bullets = []
player = Player('galaga')

def generating_enemies():
    enemies = []
    if player.level == 1:
        for row in range(0,3):
            for column in range(0,5):
                x = 40 + 80 * column
                y = 50 + 60 * row
                enemies.append(Enemy('bug', (x, y)))
        return enemies
    elif player.level == 2:
        pass
    elif player.level == 3:
        pass

enemies = generating_enemies() #generate 15 enemies
dynamites = []


def on_key_down(key):
    if key == key.SPACE and player.shoot() and player.game_state == 'play' and timer < 0:
        print('Shoot')
        sounds.bullet_pew.play()
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

        for bug in enemies:
            if bug.colliderect(bullet):
                try:
                    bullets.remove(bullet)
                except:
                    pass
                enemies.remove(bug)
                player.score += 1
                print(f'Score : {player.score}')
        
def draw_bug():
    for bug in enemies:
        bug.draw()

def draw_dynamite():
    for d in dynamites:
        d.draw()

def update_dynamite():
    for d in dynamites:
        if d.y <= 0:
            bullets.remove(d)
        else:
            d.y -= 10

        if d.colliderect(player):
            player.hp -= 1

            if player.hp <= 0:
                player.game_state = 'lose' 
            
touch_wall = False
direction  = -1 

def update_bug():
    global touch_wall, direction
    for bug in enemies:
        bug.x += 3 * direction
        if (bug.left >= WIDTH or bug.right <= 0):
            direction *= -1
            touch_wall = True
        if touch_wall:
            bug.y += 10
        
        #touching player
        if bug.colliderect(player): #touching player
            player.game_state = 'lose'  
            music.play_once('gameover')
        #shooting dynamite
        chance = random.random()*100
        if chance > 50:
            dynamites.append(Dynamite('dynamite'))

    touch_wall = False

    if len(enemies) == 0:
        player.level += 1
        #reset monster

    if len(enemies) == 0 and player.levle >= 3:
        player.game_state = 'win'
        music.play_once('win')

#This is the actual timer 
timer_start = 3
timer = timer_start

def update(dt):
    global timer, timer_start
    if player.game_state == 'play':
        timer -= dt #Count up
        # if 0 <= timer <= 3:
        #     print(round(timer))
        if timer <= 0:
            player.control()
            player.reload(dt)
            update_bullet()
            update_bug()
            update_dynamite()

def draw_countingdown(timer): 
    if 1 <= timer <= 3: #during 3-2-1
        screen.draw.text(str(round(timer)), center = (WIDTH/2, HEIGHT/2), fontsize = 50)
    if round(timer) == 0:
        screen.draw.text('Go!!!', center = (WIDTH/2, HEIGHT/2), fontsize = 50)

def restart():
    global enemies, timer
    if keyboard.RETURN:
        timer = 3
        player.game_state = 'play'
        player.hp = 3
        player.score = 0
        player.bullets = 10
        player.pos   = (WIDTH/2, HEIGHT-100)
        player.level = 1
        enemies = generating_enemies()
        print('start')

def draw():
    screen.blit('space_bg',(0,0))
    if player.game_state == 'main':
        screen.draw.text('Space Invader',center = (WIDTH/2, HEIGHT/2-150), fontsize = 80)
        screen.draw.text('Press Enter to start',center = (WIDTH/2, HEIGHT/2), fontsize = 50)
        restart()
    elif player.game_state == 'win':
        screen.draw.text('You WIN',center = (WIDTH/2, HEIGHT/2-100), fontsize = 80)
        screen.draw.text('Press Enter to start',center = (WIDTH/2, HEIGHT/2), fontsize = 50)
        restart()
    elif player.game_state == 'lose':
        screen.draw.text('You WIN',center = (WIDTH/2, HEIGHT/2-100), fontsize = 80)
        screen.draw.text('Press Enter to start',center = (WIDTH/2, HEIGHT/2), fontsize = 50)
        restart()
    elif player.game_state == 'play':
        screen.draw.text(f'Score : {player.score}', pos = (10,20) , fontsize = 40)
        screen.draw.text(f'Bullets : {player.bullets}', pos = (340,20) , fontsize = 40)
        draw_countingdown(timer)
        player.draw()
        draw_dynamite()
        draw_bullet()
        draw_bug()
    
# music.play('run')
pgzrun.go()