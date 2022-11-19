from pyfirmata import Arduino, time
from pyfirmata import OUTPUT
board = Arduino("COM5")
board.digital[13].mode = OUTPUT
i = 0
while i < 5 :
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
    i += 1
