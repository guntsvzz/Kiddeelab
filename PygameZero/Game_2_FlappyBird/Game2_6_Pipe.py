import pgzrun
import random

WIDTH,HEIGHT = 500,800
PIPE_GAP = 200
PIPE_VELOCITY = -3
BIRD_SIZE = 40

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 500)
        self.bottom_y = self.height + PIPE_GAP
        self.bottom_pipe = Actor('pipebottom', pos=(self.x, self.bottom_y), anchor=('left', 'top'))
        self.top_pipe = Actor('pipetop', pos=(self.x, self.height), anchor=('left', 'bottom'))
        self.scored = False

    def move(self):
        self.x += PIPE_VELOCITY
        self.top_pipe.x += PIPE_VELOCITY
        self.bottom_pipe.x += PIPE_VELOCITY
    
    def off_screen(self):
        return self.top_pipe.x < 0 and self.bottom_pipe.x < 0
    
class Bird(Actor):

    GRAVITY = 0.3
    FLAP_VELOCITY = -5

    def __init__(self,image_file, pos):
        super().__init__(image_file, pos)
        self.vy = 0
        self.score = 0
        self.game_state = 'start'
        self.status = True

    def update(self):
        self.y += self.vy
        self.vy += Bird.GRAVITY

        if self.vy <-3:
            self.image = 'bird2'
        else:
            self.image = 'bird1'
    
    def jump(self):
        self.vy = Bird.FLAP_VELOCITY
    
    def off_screen(self):
        return self.top > HEIGHT or self.bottom < 0
    
    def collide(self, pipe):
        if self.colliderect(pipe.bottom_pipe) or self.colliderect(pipe.top_pipe):
            return True
        
    def score_up(self, pipe):
        if self.x > pipe.x and not pipe.scored:
            self.score += 1
            pipe.scored = True
            if self.score >= 30:
                self.game_state = 'win'
    
pipes = [Pipe(x) for x in range(WIDTH, WIDTH+800, 300)]

birdSprite = Bird('bird1', pos=(200, HEIGHT//2))

def update():
    if birdSprite.game_state == 'play':
        birdSprite.update()
        
        for pipe in pipes:
            pipe.move()
            
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(pipes[-1].x + 300))
                
            if birdSprite.collide(pipe):
                print('Collision detected!')
                birdSprite.game_state ='lose'

            birdSprite.score_up(pipe)

        if birdSprite.off_screen():
            print('Bird off screen!')
            birdSprite.game_state ='lose'

        
def on_key_down(key):
    if key == key.UP and birdSprite.status == True:
        birdSprite.jump()

def draw():
    def reset():
        global pipes
        screen.draw.text('Press space to restart',center = (WIDTH/2, HEIGHT/2+50), color = (255,0,0), fontsize = 40)
        if keyboard.space:
            birdSprite.game_state = 'play'
            birdSprite.status = True
            birdSprite.pos = 200, HEIGHT//2
            pipes.clear()
            pipes = [Pipe(x) for x in range(WIDTH, WIDTH+800, 300)]
            print(f'Game Status : {birdSprite.game_state}')

    screen.blit('background',(0,0))

    if birdSprite.game_state == 'start':
        screen.draw.text('Flappy Bird',center = (WIDTH/2, HEIGHT/2), color = (255,0,0), fontsize = 40)
        screen.draw.text('Press space to restart',center = (WIDTH/2, HEIGHT/2+50), color = (255,0,0), fontsize = 40)
        if keyboard.space:
            birdSprite.game_state = 'play'
            print(f'Game Status : {birdSprite.game_state}')
        reset()

    elif birdSprite.game_state == 'lose':
        screen.draw.text('You lose',center = (WIDTH/2, HEIGHT/2), color = (255,0,0), fontsize = 40)
        reset()

    elif birdSprite.game_state == 'win':
        screen.draw.text('You win',center = (WIDTH/2, HEIGHT/2), color = (255,0,0), fontsize = 40)
        reset()

    elif birdSprite.game_state == 'play':
        birdSprite.draw()
        for pipe in pipes:
            pipe.top_pipe.draw()
            pipe.bottom_pipe.draw()
        screen.draw.text(f'{birdSprite.score}', center = (WIDTH/2, HEIGHT/2), color="white", fontsize = 60)
        
pgzrun.go()
