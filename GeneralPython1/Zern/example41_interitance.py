class Animal:
    #variable
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.hunger = 0
    #method
    def make_sound(self):
        return self.sound

    def eat(self, food):
        print(f'{self.name} is eating {food}')
        self.hunger -= 1
         
class Dog(Animal):
    pass

class Cat(Animal):
    def chase_mice(self):
        print(f'{self.name} is chasing mice!')

my_cat = Cat('Whisky','Meow')
print(my_cat.name)
print(my_cat.make_sound())
print(my_cat.eat('mice'))
print(my_cat.chase_mice())
my_dog = Dog('Fido', 'Woof')
print(my_dog.name)
print(my_dog.make_sound())
print(my_dog.eat('bone'))