hour = input('How many hour u take : ')
earn = input('How much money u get : ')

def salary(hour,earn):
    total = int(hour) * int(earn)
    return total

gun_salary = salary(hour, earn)
zern_salary = salary(8, 1000)

print(gun_salary)
print(zern_salary)