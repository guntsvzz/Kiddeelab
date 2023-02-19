#creating function
def num():
    x = 300 #local
    print(x)
    
x = 200 #global
#calling function
num() #300
print(x) #200
