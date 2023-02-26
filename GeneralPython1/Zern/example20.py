#For loop
#Format:
#for something in array:
#   task
# array = [],(), {}
print('----list--------')
list_number = [5,4,6,8] 
for number in list_number:
    print(number)
print('----tuple--------')
tuple_number = (7,4,9,0)
for number in tuple_number:
    print(number)
print('----tuple--------')
set_number = {1,3,5,5,2,0} #ordering unique number
for number in set_number:
    print(number)
#print 1-100
#function range
print(range(0,10,1)) #start,stop(exclude num),step
#[0,1,2,...,100]
for i in range(0,10,1):
    print(i)
pets = ['cat','dog','goldfish']
for p in pets:
    print(p)
#Test
#0-50
for i in range(0,51,1):
    print(i)
#50-0
for i in range(50,-1,-1):
    print(i)
#0-50 even number
for i in range(0,51,2): #random.randrange(start,stop,step)
    print(i)
#0-50 odd number
for i in range(1,51,2):
    print(i)

#anything that involve with array, choose for loop
#anything that repeat checking, choose while loop
