#Import data
from pyfirmata import Arduino,time
from pyfirmata import OUTPUT
#Configuration
board = Arduino("COM5")
board.digital[10].mode = OUTPUT
board.digital[11].mode = OUTPUT
print('Blinking 1 Seconds')
#Code
i = 0
while i < 5:
    for pin in range(10,14,1):
        board.digital[pin].write(1)
        time.sleep(1)
        board.digital[pin].write(0)
        time.sleep(1)
    i = i + 1
