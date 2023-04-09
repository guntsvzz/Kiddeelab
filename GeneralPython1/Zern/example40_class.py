class Person():
    #properly = variable = attribute
    #class variables
    species = 'Homo Sapien' 
    #instance variables
    def __init__(self, name, age, job): #classify which object have to use these instance variables
        self.name = name 
        self.age = age
        self.job = job
    #method
    def greeting(self):
        return f'Hello I\'m {self.name}'
    
p1 = Person('Gun',23,'Teacher')
print(p1.species)
print(p1.name)
print(p1.greeting())
p2 = Person('Zern',12,'Student')
print(p2.species)
print(p2.name)
print(p2.greeting())