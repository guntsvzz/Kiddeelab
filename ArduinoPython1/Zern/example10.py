from pyfirmata import OUTPUT, Arduino, time

board = Arduino("COM3")
board.digital[3].mode = OUTPUT

def buzzer():
    board.digital[3].write(1)#on
    time.sleep(1) #wait 1 s
    board.digital[3].write(0)#off
    time.sleep(5) #wait 5 s

while True :
    buzzer()