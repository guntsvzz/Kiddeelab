import random
a = random.randrange(0,1000,1) #0-1000 divide 10 
b = random.randrange(0,500,1)  #0-500 divide 3
c = random.randrange(0,100,1)  #0-100 divide 5
print(a,b,c)
#minimum
minimum = min(a,b,c)
#maximum
maximum = max(a,b,c)
print(minimum, maximum)