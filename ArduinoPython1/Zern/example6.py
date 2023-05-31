from pyfirmata import Arduino, time, OUTPUT

board = Arduino("COM4") #class
#LED is digital OUTPUT
board.digital[10].mode = OUTPUT
board.digital[11].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[13].mode = OUTPUT

while True:
    board.digital[10].write(1)
    board.digital[11].write(1)
    board.digital[12].write(1)
    board.digital[13].write(1)
