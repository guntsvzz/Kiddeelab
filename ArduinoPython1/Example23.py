from pyfirmata import Arduino,time
from pyfirmata import INPUT,util

board = Arduino("COM7")
board.analog[0].mode = INPUT
#using for INPUT
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
time.sleep(1)

while(1):
    potentiometer = board.analog[0].read()*1023 #0-1
    print(potentiometer)
    if potentiometer > 0 and potentiometer < 255:
        print("Part1")
    if potentiometer > 256 and potentiometer < 512:
        print("Part2")
    time.sleep(1)
