from pyfirmata import Arduino, time, OUTPUT

board = Arduino("COM4") #class
#LED is digital OUTPUT
board.digital[11].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[13].mode = OUTPUT
i = 0
while i < 5:
    #tun on
    board.digital[11].write(0) #off Low
    board.digital[12].write(1) #0n High
    board.digital[13].write(1) #0n High
    time.sleep(1) #delay
    #turn off
    board.digital[11].write(1) #on Low 
    board.digital[12].write(0) #off High
    board.digital[13].write(0) #off High
    time.sleep(1)
    i += 1