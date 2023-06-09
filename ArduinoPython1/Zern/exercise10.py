from pyfirmata import Arduino, time, OUTPUT

board = Arduino("COM9")
for pin in range(10,14,1):
    board.digital[pin].mode = OUTPUT

def ON_ACTHIGH():
    pin = 10
    while pin < 14:
        #on
        time.sleep(0.5)
        #off 
        pin+=1

def FOR_ON_ACTHIGH():
    for pin in range(10,14,1):
        #on
        time.sleep(0.5)
        #off

# ON_ACTHIGH()
FOR_ON_ACTHIGH()