a = float(input('Enter the value a : '))
b = float(input('Enter the value b : '))

#creating function
def operation(x,y): 
    print('Here is the results')
    print('A + B is equal', x+y)
    print('A - B is equal', x-y)
    print('A * B is equal', x*y)
    print('A / B is equal', x/y)
    
#calling function
operation(a,b)
operation(b,a)