#format nameoffunction(agrument)
#data type
#integer(int) whole number 5 6 -1
#float decimal number 3.4 0.6 -1.2 1.0
#string(str) text 'a' 'gun' '1'
#boolean True,False (1,0)

print('hello world')
print(5)
print('5')
test = 523
test = 'Gun'
print(test)
print(True)
a,b,c,d = 4,3,2,1
print(a,b,c,d)

#operation 
result = a + b
print(result)
result2 = 1 + 5.5
print(result2)
result3 = 'apple' + '6' #str = text text cannot do Math
print(result3)
# result4 = '5' + 5 #str + int = wrong
# print(result4)

#casting
x,y,z = 5,'1', 2.5

#case 1 str (text) -> int or float (number)
print(y)
print(int(y))
print(float(y))

print(type(y))
print(type(int(y)))
print(type(float(y)))

#case 2 int or float (number) -> str (text)
print(z) 
print(int(z)) #it cut all any decimal number
print(str(z)) 

result4 = int('5') * 5
print(result4)
result5 = int('100') / float('20.3')
print(result5) #120.3

# summary 
# print show output
# int float str boolean 
# str + str = strstr
# str + int or float = wrong
# casting convert one by one