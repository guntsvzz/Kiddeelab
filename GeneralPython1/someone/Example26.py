text = 'Hello Kiddee Lab Lab'
text2 = '1234'
#count method
a1 = text.count('d')
print(a1)
a2 = text.count('d',1,9) #value, start ,end
print(a2)
#replace method
a3 = text.replace('Lab','Bye') #old,new
print(a3)
a4 = text.replace('Lab','Bye',1) #old,new,count
print(a4)
#split method
a5 = text.split() #separator ,maxsplit
print(a5)
a6 = text.split(',') #separator ,maxsplit
print(a6)
a7 = text.upper()
print(a7)
a8 = text.lower()
print(a8)
a9 = text.capitalize()
print(a9)
a10 = text.isalpha() #all string is alphabet or not
print(a10)
a11 = text2.isdigit() #all string is number or not
print(a11)
