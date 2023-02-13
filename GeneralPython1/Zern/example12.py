import random
print(random.random()) #0-1
a = random.random()*100
print(a) #0-100
print(random.random()*100)
#function randint()
print(random.randint(1,10)) #randint(start,stop(include)) 1-10
#function randrange()
print(random.randrange(1,10,1)) #randrange(start,stop(exclude),step) 1-9
