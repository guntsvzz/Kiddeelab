from pyfirmata import Arduino,time
from pyfirmata import OUTPUT
from pyfirmata import INPUT, util
import random

board = Arduino("COM7")
#switch
board.digital[3].mode = INPUT
#buzzer
board.digital[5].mode = OUTPUT 
#7segment
for i in range(7,14,1):
    board.digital[i].mode = OUTPUT
#using for INPUT
it = util.Iterator(board)
it.start()
time.sleep(1)
#Array2D
number = [[1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]]

print("ready to start")

while(1):
    SW1 = board.digital[3].read()
    if SW1 == 1:
        rd = random.randrange(0,10,1) #(start,stop,step)
        print('Got Number',rd)
        for y in range(7): #column
            board.digital[y+7].write(number[rd][y])
        time.sleep(1)
        board.digital[5].write(1)
        time.sleep(0.5)
        board.digital[5].write(0)
        time.sleep(2.5)
    else: #SW = 0
        for x in range(10): #row
            for y in range(7): #column
                board.digital[y+7].write(number[x][y])
                time.sleep(0.1)
