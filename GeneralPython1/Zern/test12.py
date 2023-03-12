#kiddeelab 5 courses
#set cannot use index
#list , tuple can index
kdl_course = ['Tinkamo','Movie','mBot','Halocode','Python']
age = int(input('How old are you ? :'))
print('The recommended courses :')
if 4 <= age <=5: #1st chain operation
    print(kdl_course[0])
elif age >= 6 and age <= 9: #2nd logic operation
    print(kdl_course[0], kdl_course[1], kdl_course[2])
elif age in range(10,13): #3rd range function
    print(kdl_course[2], kdl_course[1], kdl_course[3])
elif age >= 13: #4th 
    print(kdl_course[1], kdl_course[3], kdl_course[4])