import random
import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = 'pong'

# a color used to draw things
MAIN_COLOR = 'red'

# width and height of a player paddle
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

# radius of the tennis ball
TENNIS_BALL_RADIUS = 10

LEFT_PLAYER = "left"
RIGHT_PLAYER = "right"

class Paddle(Rect):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self):
        screen.draw.filled_rect(self, MAIN_COLOR)

class TennisBall():
    def __init__(self, start_pos, dt):
        self.x, self.y = start_pos
        self.dx = self.dy = dt

    @property
    def pos(self):
        return (self.x, self.y)

    def draw(self):
        screen.draw.filled_circle(self.pos, TENNIS_BALL_RADIUS, MAIN_COLOR)

class Game():

    def __init__(self, player):
        self.active_player = player
        self.score_left = 0
        self.score_right = 0

        self.in_progress = False
        self.computer_acting = False

        # position paddles in the middle of the screen
        middle = HEIGHT/2 - PADDLE_HEIGHT/2
        self.left_paddle = Paddle(20, middle)
        self.right_paddle = Paddle(WIDTH-40, middle)

        self.set_ball(self.ball_pos)

    @property
    def ball_pos(self):
        if self.active_player == LEFT_PLAYER:
            return (20 + PADDLE_WIDTH + 10, self.left_paddle.centery)
        else:
            return (WIDTH - 35 - PADDLE_WIDTH, self.right_paddle.centery)

    def set_ball(self, pos):
        # a ball is set on the paddle of last player that got a point
        dt = 5 if self.active_player == LEFT_PLAYER else -5
        self.tennis_ball = TennisBall(pos, dt)

    def draw(self):
        # slightly gray background
        screen.fill((64, 64, 64))

        # show the score for the left player
        screen.draw.text('Computer: {}'.format(self.score_left),
            color=MAIN_COLOR,
            center=(WIDTH/4 - 20, 20),
            fontsize=48
        )

        # show the score for the right player
        screen.draw.text('Player: {}'.format(self.score_right),
            color=MAIN_COLOR,
            center=(WIDTH/2 + WIDTH/4 - 20, 20),
            fontsize=48
        )

        # a dividing line
        screen.draw.line(
            (WIDTH/2, 40), (WIDTH/2, HEIGHT-40), 
            color=MAIN_COLOR
        )

        if self.score_left == 11:
            pass
        elif self.score_right == 11:
            pass
        else:
            self.left_paddle.draw()
            self.right_paddle.draw()
            self.tennis_ball.draw()

# first player is chosen randomly
player = LEFT_PLAYER if random.randint(0, 1000) % 2 == 0 else RIGHT_PLAYER
game = Game(player)

def draw():
    game.draw()

def update():
    pass

pgzrun.go()