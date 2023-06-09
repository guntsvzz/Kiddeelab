from pyfirmata import OUTPUT, Arduino, time

board = Arduino("COM3")
board.digital[3].mode = OUTPUT

while True :
    board.digital[3].write(1)#on
    time.sleep(0.1)#wait 0.1 s
    board.digital[3].write(0)#off
    time.sleep(2)#wait 2 s