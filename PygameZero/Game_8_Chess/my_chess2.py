import pgzrun

tile_size = 50

tiles = {0: 'square'}

squares = [[0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]

WIDTH = tile_size * len(squares[0])
HEIGHT = tile_size * len(squares)

pawn_white1 = False
pawn_white2 = False
pawn_white3 = False
pawn_black1 = False
rook_white1 = False
knight_white1 = False

y_w_pawn1_1 = False
y_w_pawn1_2 = False

y_w_rook1_1 = False
y_w_rook1_2 = False
y_w_rook1_3 = False
y_w_rook1_4 = False
y_w_rook1_5 = False
y_w_rook1_6 = False
y_w_rook1_7 = False


w_pawn1 = Actor('w_pawn')
w_pawn1.anchor = (-7,0)
w_pawn1.pos = (0*tile_size,1*tile_size)
x_w_pawn1 = w_pawn1.x// tile_size
y_w_pawn1 = w_pawn1.y// tile_size
print(w_pawn1.x,w_pawn1.y)

w_pawn2 = Actor('w_pawn')
w_pawn2.anchor = (-7,0)
w_pawn2.pos = (1*tile_size,1*tile_size)
x_w_pawn2 = w_pawn2.x// tile_size
y_w_pawn2 = w_pawn2.y// tile_size
print(w_pawn2.x,w_pawn2.y)

w_pawn3 = Actor('w_pawn')
w_pawn3.anchor = (-7,0)
w_pawn3.pos = (2*tile_size,1*tile_size)
x_w_pawn3 = w_pawn3.x// tile_size
y_w_pawn3 = w_pawn3.y// tile_size
print(w_pawn3.x,w_pawn3.y)

b_pawn1 = Actor('b_pawn')
b_pawn1.anchor = (-7,0)
b_pawn1.pos = (0*tile_size,6*tile_size)
x_b_pawn1 = b_pawn1.x// tile_size
y_b_pawn1 = b_pawn1.y// tile_size
print(b_pawn1.x,b_pawn1.y)

w_rook1 = Actor('w_rook')
w_rook1.anchor = (-7,0)
w_rook1.pos = (0*tile_size,0*tile_size)
x_w_rook1 = w_rook1.x// tile_size
y_w_rook1 = w_rook1.y// tile_size
print(w_rook1.x, w_rook1.y)

w_knight1 = Actor('w_knight')
w_knight1.anchor = (-7,0)
w_knight1.pos = (1*tile_size,0*tile_size)
x_w_knight1 = w_knight1.x// tile_size
y_w_knight1 = w_knight1.y// tile_size
print(w_knight1.x, w_knight1.y)

def on_mouse_down(pos):
    global pawn_white1, x_w_pawn1, y_w_pawn1, pawn_white2 , x_w_pawn2, y_w_pawn2, pawn_white3 , x_w_pawn3, y_w_pawn3
    global pawn_black1 , x_b_pawn1, y_b_pawn1
    global rook_white1, x_w_rook1, y_w_rook1
    global knight_white1, x_w_knight1, y_w_knight1

    global y_w_pawn1_2, y_w_pawn1_1
    global y_w_rook1_7, y_w_rook1_6, y_w_rook1_5, y_w_rook1_4, y_w_rook1_3, y_w_rook1_2, y_w_rook1_1
    x = pos[0] // tile_size
    y = pos[1] // tile_size
    x_w_pawn1 = w_pawn1.x// tile_size
    y_w_pawn1 = w_pawn1.y// tile_size
    x_w_pawn2 = w_pawn2.x// tile_size
    y_w_pawn2 = w_pawn2.y// tile_size
    x_w_pawn3 = w_pawn3.x// tile_size
    y_w_pawn3 = w_pawn3.y// tile_size
    x_b_pawn1 = b_pawn1.x// tile_size
    y_b_pawn1 = b_pawn1.y// tile_size
    x_w_rook1 = w_rook1.x// tile_size
    y_w_rook1 = w_rook1.y// tile_size
    x_w_knight1 = w_knight1.x// tile_size
    y_w_knight1 = w_knight1.y// tile_size
    if x == x_w_pawn1 and y == y_w_pawn1:
        print('white_pawn1')
        pawn_white1 = True
        pawn_white2 = False
        pawn_white3 = False
    if x == x_w_pawn2 and y == y_w_pawn2:
        print('white_pawn2')
        pawn_white2 = True
        pawn_white1 = False
        pawn_white3 = False
    if x == x_w_pawn3 and y == y_w_pawn3:
        print('white_pawn2')
        pawn_white3 = True
        pawn_white1 = False
        pawn_white2 = False
    if x == x_b_pawn1 and y == y_b_pawn1:
        print('black_pawn1')
        pawn_black1 = True
    if x == x_w_rook1 and y == y_w_rook1:
        print('white_rook1')
        rook_white1 = True
    if x == x_w_knight1 and y == y_w_knight1:
        print('white knight1')
        knight_white1 = True
  
    if pawn_white1:
        y = pos[1] // tile_size
        print(x,y)
        if y == y_w_pawn1+1 and y_w_pawn1_1:
            w_pawn1.pos = (0*tile_size,y*tile_size)
            pawn_white1 = False
            y_w_pawn1_1 = False
        if y == y_w_pawn1+2 and y_w_pawn1_2:
            w_pawn1.pos = (0*tile_size,y*tile_size)
            pawn_white1 = False
            y_w_pawn1_2 = False
    
    if pawn_white2:
        y = pos[1] // tile_size
        print(x,y)
        if y == y_w_pawn2+1:
            w_pawn2.pos = (1*tile_size,y*tile_size)
            pawn_white2 = False
        if y == y_w_pawn2+2:
            w_pawn2.pos = (1*tile_size,y*tile_size)
            pawn_white2 = False
    
    if pawn_white3:
        y = pos[1] // tile_size
        print(x,y)
        if y == y_w_pawn3+1:
            w_pawn3.pos = (2*tile_size,y*tile_size)
            pawn_white3 = False
        if y == y_w_pawn3+2:
            w_pawn3.pos = (2*tile_size,y*tile_size)
            pawn_white3 = False
    
    if rook_white1:
        y = pos[1] // tile_size
        if y == y_w_rook1+1 and y_w_rook1_1:
            w_rook1.pos = (0*tile_size,y*tile_size)
            rook_white1 = False
            y_w_rook1_1 = False
    


  

def draw():
    def squareGeneration():
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    color = (0, 0, 0)
                else:
                    color = (255, 255, 255) 
                Box = Rect ((x*tile_size, y*tile_size), (tile_size, tile_size))
                screen.draw.filled_rect(Box,color)

    def hightlighted_white_pawn():
        global y_w_pawn1_2, y_w_pawn1_1
        if pawn_white1 :
            if y_w_pawn1+2 != y_b_pawn1 and y_w_pawn1+1 != y_b_pawn1:
                for y_w_p1 in range(int(y_w_pawn1+1),int(y_w_pawn1+3)):               
                    Box = Rect ((x_w_pawn1*tile_size, y_w_p1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                    print(1)
                y_w_pawn1_2 = True
                y_w_pawn1_1 = True
                print(y_w_pawn1_2)
            elif y_w_pawn1+1 != y_b_pawn1:
                for y_w_p1 in range(int(y_w_pawn1+1),int(y_w_pawn1+2)):               
                    Box = Rect ((x_w_pawn1*tile_size, y_w_p1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                    print(y_w_pawn1+1)
                y_w_pawn1_1 = True
                print(y_w_pawn1_1)
            elif y_w_pawn1+1 == y_b_pawn1:
                squareGeneration()
            
             
        
        elif pawn_white2 :
            for y_w_p2 in range(int(y_w_pawn2+1),int(y_w_pawn2+3)):
                Box = Rect ((x_w_pawn2*tile_size, y_w_p2*tile_size), (tile_size, tile_size))
                screen.draw.filled_rect(Box,'red')
                print(2)

        elif pawn_white3:
            for y_w_p3 in range(int(y_w_pawn3+1),int(y_w_pawn3+3)):
                Box = Rect ((x_w_pawn3*tile_size, y_w_p3*tile_size), (tile_size, tile_size))
                screen.draw.filled_rect(Box,'green')
                print(3)
        
        else:
            squareGeneration()
        
    def hightlighted_black_pawn():
        if pawn_black1 :
            for y_b_p1 in range(int(y_b_pawn1-2),int(y_b_pawn1)):
                Box = Rect ((x_b_pawn1*tile_size, y_b_p1*tile_size), (tile_size, tile_size))
                screen.draw.filled_rect(Box,'yellow')
                print(1)

    def hightlighted_white_rook():
        global y_w_rook1_7, y_w_rook1_6, y_w_rook1_5, y_w_rook1_4, y_w_rook1_3, y_w_rook1_2, y_w_rook1_1
        if rook_white1:
            if y_w_rook1+1 == y_w_pawn1:
                squareGeneration()  
            elif y_w_rook1+7 != y_w_pawn1 and y_w_rook1 +6 != y_w_pawn1 and y_w_rook1+5 != y_w_pawn1 and y_w_rook1+4 != y_w_pawn1 and y_w_rook1+3 != y_w_pawn1 and y_w_rook1+2 != y_w_pawn1 and y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(len(squares))):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                y_w_rook1_2 = True
                y_w_rook1_3 = True
                y_w_rook1_4 = True
                y_w_rook1_5 = True
                y_w_rook1_6 = True
                y_w_rook1_7 = True
                print(1)
            elif y_w_rook1 +6 != y_w_pawn1 and y_w_rook1+5 != y_w_pawn1 and y_w_rook1+4 != y_w_pawn1 and y_w_rook1+3 != y_w_pawn1 and y_w_rook1+2 != y_w_pawn1 and y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(y_w_rook1+7)):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                y_w_rook1_2 = True
                y_w_rook1_3 = True
                y_w_rook1_4 = True
                y_w_rook1_5 = True
                y_w_rook1_6 = True
                print(1)
            elif y_w_rook1+5 != y_w_pawn1 and y_w_rook1+4 != y_w_pawn1 and y_w_rook1+3 != y_w_pawn1 and y_w_rook1+2 != y_w_pawn1 and y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(y_w_rook1+6)):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                y_w_rook1_2 = True
                y_w_rook1_3 = True
                y_w_rook1_4 = True
                y_w_rook1_5 = True
                print(1)
            elif y_w_rook1+4 != y_w_pawn1 and y_w_rook1+3 != y_w_pawn1 and y_w_rook1+2 != y_w_pawn1 and y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(y_w_rook1+5)):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                y_w_rook1_2 = True
                y_w_rook1_3 = True
                y_w_rook1_4 = True
                print(1)
            elif y_w_rook1+3 != y_w_pawn1 and y_w_rook1+2 != y_w_pawn1 and y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(y_w_rook1+4)):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                y_w_rook1_2 = True
                y_w_rook1_3 = True
                print(1) 
            elif y_w_rook1+2 != y_w_pawn1 and y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(y_w_rook1+3)):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                y_w_rook1_2 = True
                print(1)
            elif y_w_rook1+1 != y_w_pawn1:
                for y_w_r1 in range(int(y_w_rook1+1),int(y_w_rook1+2)):
                    Box = Rect ((x_w_rook1*tile_size, y_w_r1*tile_size), (tile_size, tile_size))
                    screen.draw.filled_rect(Box,'yellow')
                y_w_rook1_1 = True
                print(1)
              
            for x_w_r1 in range(int(x_w_rook1+1), int(len(squares[0]))):
                Box = Rect ((x_w_r1*tile_size, y_w_rook1*tile_size), (tile_size, tile_size))
                screen.draw.filled_rect(Box,'yellow')
                print(2)
    def hightlighted_white_knight():
        if knight_white1:
            pass
# col = int(input())
# row = int(input())
# colN = int(input())
# rowN = int(input())

# if (colN == col + 1 or colN == col - 1) and (rowN == row - 2 or rowN == row + 2):
# print ("YES")
# elif (rowN == row + 1 or rowN == row - 1) and (colN == col - 2 or colN == col + 2):
# print ("YES")
# else:
# print ("NO")


    squareGeneration()
    hightlighted_white_pawn()
    hightlighted_black_pawn()
    hightlighted_white_rook()
    w_pawn1.draw()
    w_pawn2.draw()
    w_pawn3.draw()
    b_pawn1.draw()
    w_rook1.draw()
    w_knight1.draw()

pgzrun.go()
