import math
import Example42Parent
#child class
class Calculation(Example42Parent.Shape):
    #method without agrument with return
    def rectangle(self):
        return (self.width*self.height)
    def triangle(self):
        return (0.5*self.width*self.height)   
    def cricle(self):
        return round((math.pi*self.radius**2),2)
    
#input function
w = int(input('Insert Width'))
h = int(input('Insert Heigth'))
r = int(input('Insert Radius'))
#Calling object
result = Calculation(w,h,r)
#result
print(result.rectangle())
print(result.triangle())
print(result.cricle())
    
