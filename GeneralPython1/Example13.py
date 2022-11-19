import random
#random method #float
#module.method()/function()
a = random.random() #random 0-1
print(a)
b = int(random.random()*500)
print(b)
#randrange method #int
#random.randrange(start,stop,step)
c = random.randrange(1,12) #start,stop
print(c)
d = random.randrange(1,12,2) #start,stop,step
print(d)
#uniform method #float
e = random.uniform(1,10) 
print(e)
