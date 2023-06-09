#Import data
from pyfirmata import Arduino,time
from pyfirmata import OUTPUT
#Configuration
board = Arduino("COM5")
board.digital[13].mode = OUTPUT
print('Blinking 1 Seconds')
#Code
i = 0
while i < 5:
    #ActiveHigh
    board.digital[13].write(1) #TurnOn
    time.sleep(1)
    board.digital[13].write(0) #TurnOff
    time.sleep(1)
    i = i + 1
