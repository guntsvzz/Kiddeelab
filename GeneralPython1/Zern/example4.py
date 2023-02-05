a = True
b = False
c = True

d = not((a and b) or (not c or a))
print(d) 

#summary 
#if there are both True in and, it give True
#if there is at least one True in or, it give True
#not will return opposite value