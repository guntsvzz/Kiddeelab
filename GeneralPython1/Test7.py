#input
M = int(input('Please input your Maths result:'))
S = int(input('Please input your Science result:'))
E = int(input('Please input your English result:'))
T = int(input('Please input your Thai result:'))
course = int(M,S,E,T) #tuple
total = course[0]+course[1]+course[2]+course[3]
print('Your total score is',total,'out of 400')
percentage = total*100/400
print('In percentage, you obtained',percentage,'%')
