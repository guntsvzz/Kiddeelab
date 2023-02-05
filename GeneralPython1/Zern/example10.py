def Salary(hr,rate,name):
    return hr*rate, name

gun = Salary(10,200,'Gun')
reef = Salary(5,200,'reef')
boss = Salary(8,200,'boss')
print(gun)
print(reef)
print(boss)

sum = gun[0]+reef[0]+boss[0]
print(sum)