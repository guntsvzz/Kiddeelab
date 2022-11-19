time = int(input('How many times?:'))
for i in range(1,time+1,1):
    print('No.',i)
    star = int(input('Enter star:'))
    for j in range(1,star+1,1):
        print('*',end='')
    print()
    
