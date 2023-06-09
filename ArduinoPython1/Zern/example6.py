from pyfirmata import OUTPUT, Arduino, time

board = Arduino("COM3")
# board.digital[10].mode = OUTPUT
# board.digital[11].mode = OUTPUT
# board.digital[12].mode = OUTPUT
# board.digital[13].mode = OUTPUT
for pin in range(10,14,1): #start,end(exclude),step
    board.digital[pin].mode = OUTPUT

while True:
    board.digital[10].write(1) #10 Active High
    board.digital[11].write(0) #11
    board.digital[12].write(0) #12
    board.digital[13].write(0) #13
    time.sleep(1)
    board.digital[10].write(0) #10 Active High
    board.digital[11].write(1) #11
    board.digital[12].write(0) #12
    board.digital[13].write(0) #13
    time.sleep(1)
    board.digital[10].write(0) #10 Active High
    board.digital[11].write(0) #11
    board.digital[12].write(1) #12
    board.digital[13].write(0) #13
    time.sleep(1)
    board.digital[10].write(0) #10 Active High
    board.digital[11].write(0) #11
    board.digital[12].write(0) #12
    board.digital[13].write(1) #13
    time.sleep(1)