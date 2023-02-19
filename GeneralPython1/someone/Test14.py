class House():
    #class variable
    unit = 'm2'
    def __init__(self,owner,price,stdheight,stdwidth)
        #instance variable
        self,owner = owner 
        self.price = price
        self.stdheight = stdheight
        self.stdwidth = stdwidth
    #method
    def area(self):
        cal = self.stdheight*self.stdwidth
        print(self.owner,'house has area of',cal,'with',self.price)
        
#Create object
Anthony = House('Anthony',890000,20,10)
Third = House('Third',1100000,15,15)
Gun = House('Gun',600000,10,10)
#calling method
Anthony.area()
Third.area()
Gun.area()
