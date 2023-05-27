import pgzrun

squares = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]

tile_size = 50
tiles = {0: 'square'}
WIDTH = tile_size * len(squares[0])
HEIGHT = tile_size * len(squares)

class Chess(Actor):
    def __init__(self, img_file,pos, anchor = (-7,0)):
        super().__init__(img_file, pos, anchor)
        self.white = ['w_pawn', 'w_rook', 'w_knight']
        self.black = ['b_pawn']

    def move(self):
        if self.image == 'w_pawn' or self.image == 'b_pawn':
            pass
        elif self.image == 'w_rook' or self.image == 'b_rook':
            pass
        elif self.image == 'w_knight' or self.image == 'b_knight':
            pass

def draw():
    pass

def update():
    pass

pgzrun.go()