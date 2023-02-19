class Person():
    #class variable
    species = 'Homo sapien'
    def __init__(self,name,age):
        #instance variable
        self.name = name
        self.age = age
    #def __del__(self):
    #    print('deleted')
    #Method
    def sleep(self,time): #function with agrument wihtout return
        print(self.name,'has slept around',time,'hours')
    def eat(self,calories):
        print(self.name,'has eaten around',calories,'calories')
        
#calling from object
gun = Person('Gun',22)
reef = Person('Reef',25)
print(gun.name,gun.age,gun.species)
print(reef.name,reef.age,reef.species)
gun.sleep(3)
gun.eat(1800) 
reef.sleep(7) #method
reef.eat(2000) 
#del gun
#print(gun.name)
#calling from class
#print(Person)
#print(Person.species)
