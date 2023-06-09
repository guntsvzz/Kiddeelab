##import library
from pyfirmata import INPUT, OUTPUT
from pyfirmata import util, time, Arduino
##set configuration
board = Arduino("/dev/cu.usbmodem1101")
board.digital[3].mode = INPUT
board.digital[5].mode = OUTPUT
for pin in range(7,14):
    board.digital[pin].mode = OUTPUT
iter = util.Iterator(board)
iter.start()

numberCC = [
    [1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]]

##loop
while True: 
    sw1 = board.digital[3].read() ##check switch
    sw2 = board.digital[4].read() ##check switch
    if sw1 == 1: ###condition
        ##7-segment
        for row in range(len(numberCC)):
            for idx, pin in enumerate(range(7,14)):
                board.digital[pin].write(numberCC[row][idx])
            time.sleep(0.5)
        ##buzzer
        board.digital[5].write(1) #turn on buzzer
        time.sleep(1)
        board.digital[5].write(0) #turn off buzzer
        ## turn off LED
        for pin in range(7,14):
            board.digital[pin].write(0)
    elif sw2 == 1: ###condition
        ##7-segment
        for row in range(len(numberCC)-1,-1,-1):
            for idx, pin in enumerate(range(7,14)):
                board.digital[pin].write(numberCC[row][idx])
            time.sleep(0.5)
        ##buzzer
        board.digital[5].write(1) #turn on buzzer
        time.sleep(1)
        board.digital[5].write(0) #turn off buzzer
        ## turn off LED
        for pin in range(7,14):
            board.digital[pin].write(0)