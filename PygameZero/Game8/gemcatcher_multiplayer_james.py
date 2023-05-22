import pgzrun
import random

WIDTH = 800
HEIGHT = 600

scores=[0,0,0]
player=1

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
game_over = False


def play_again():
    global score, game_over, player
    gem.x = random.randint(20, 780)
    gem.y = 0
    if player==1:
        player=2
    else:
        player=1
    game_over = False
    score = 0

        

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def update():
    global score, game_over, player

    if keyboard.s:
        #game_over = False
        play_again()
        

    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        game_over = True
        #update the score
        scores[player]=score
        #print(scores)
        
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1

def draw():
    global player
    screen.fill((80,0,70))
    if game_over:
        screen.draw.text('Game Over', (300, 300), color=(255,255,255), fontsize=60)
        screen.draw.text("Player 1's Score: " + str(scores[1]) , (100, 150), color=(255,255,255), fontsize=60)
        screen.draw.text("Player 2's Score: " + str(scores[2]) , (100, 200), color=(255,255,255), fontsize=60)
        if (scores[1] > scores[2]):
            screen.draw.text("Player 1 is leading!" , (100, 250), color=(255,255,255), fontsize=60)
        else:
            screen.draw.text("Player 2 is leading!" , (100, 250), color=(255,255,255), fontsize=60)

            

        
        #screen.draw.text('Score: ' + str(score) , (300, 350), color=(255,255,255), fontsize=60)
        screen.draw.text("Player "+str(player)+"'s Score: " + str(score) , (300, 350), color=(255,255,255), fontsize=60)
        screen.draw.text("Player "+str(player)+"'s Score: " + str(score) , (300, 350), color=(255,255,255), fontsize=60)

        screen.draw.text('Press S for next player ', (300, 400), color=(255,0,0), fontsize=30)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score) + '  Player: ' + str(player), (15,10), color=(255,255,255), fontsize=30)


 


pgzrun.go() # Must be last line
