age = int(input('How old is your kid?'))
course = ['Tinkamo','mBot','Movie','Halocode','Python']

if (age >= 13): #13-18
    print(', '.join(course[2:5])) 
elif (age >= 10): #10-12
    print(', '.join(course[1:4]))
elif (age >= 6): #6-9
    print(', '.join(course[0:3]))
elif (age >= 4): #4-5
    print(course[0])
