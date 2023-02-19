class Pet:
    #Class Variable
    animal = 'dog' 
    #The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable 
        self.breed = breed
        self.color = color 
#Objects of Pet class
Rodger = Pet('Pug', 'brown')
Buzo = Pet('Bulldog', 'black')
print('Rodger details:') 
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
print('\nBuzo details:') 
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
