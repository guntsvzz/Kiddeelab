# #Basic Data type
# True, False #Boolean
# 'Tyler','Gun' #string
# 1,2,-5,-10 #integer
# 1.0,5.5,10.01 #float
# #Array Data type
# tyler = [1,2,3,4,'five'] #list
# gun = (1,2,3,4,'five') #tuple cannot change item
# a = {1,2,3,3,4} #set #1,2,3,4
# hero = {
#     'hp' : 100,
#     'normal attack' : 20,
#     'hard attack' : 100
# } #dictionary key:value
 
# hero['hp'] #->100

# #Function 
# def name(nickname): #attribute
#    print('My name is', nickname) 

# name('Gun') #recalling

#loops while vs for

#for - > good is for array and range
#[1, 2, 3, ... ,1000]
for i in range(1,11,1):
    print(i)
for i in range(1,11,2):
    print(i)

#while -> finite loop -> always checking
#False -> Stop
# answer = input('Answer Y/N :')
# while answer != 'yes':
#     answer = input('Answer Y/N :')

# score = 15
# if score >= 20:
#     print('A')
# elif score >= 15:
#     print('B')
# else:
#     print('F')

