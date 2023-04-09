class House:
    unit = 'm2'
    def __init__(self, owner, price = 1000000, stdHeight = 10, stdWidth = 10):
        self.owner = owner
        self.price = price
        self.stdHeight = stdHeight
        self.stdWidth = stdWidth 

    def own(self):
        return f'Owner is {self.owner}'
    
    def area(self):
        return self.stdHeight * self.stdHeight
    
h1 = House('Anthony', 800000, 9, 9)
h2 = House('Gun')
h3 = House('Benz', 2000000, 10, 20)

print(h3.own())