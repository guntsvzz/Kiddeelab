# print('a')
# print()
# print('b')
#creating function
def area():
    w,h = 10,10
    a = w*h
    print(a)
def area2(w,h):
    a = w*h
    print(a)
#setting default
def area3(w=5,h=10):
    a = w*h
    print(a)
def area4(w,h=10):
    a = w*h
    print(a)
#calling function
area()
area2(2,3) #w=2,h=3
area3()
area4(5,2)