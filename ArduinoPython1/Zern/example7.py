from pyfirmata import OUTPUT, Arduino, time

board = Arduino("COM3")
# board.digital[10].mode = OUTPUT
# board.digital[11].mode = OUTPUT
# board.digital[12].mode = OUTPUT
# board.digital[13].mode = OUTPUT
for pin in range(10,14,1): #start,end(exclude),step
    board.digital[pin].mode = OUTPUT

while True:
    for pin in range(10,14,1): #start,end(exclude),step
        board.digital[pin].write(1)
        time.sleep(1)
        board.digital[pin].write(0)
