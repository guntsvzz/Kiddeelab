c = float(input('Enter Temperature in Celsius:'))  #string -> float
f = float(input('Enter Temperature in Fahrenheit:'))

def c2f(c):
    equation = ((9/5) * c) + 32
    return equation
    
def f2c(f):
    equation = (f -32)*(5/9)
    return equation

print(c2f(c))
print(f2c(f))