#### Vaccine
VaccineInfo = {
    'Name'  : ['Pfizer', 'Moderna', 'Sinopharm', 'Sinovac'],
    'Price' : [3000,      3300,      3400,        0]
}
print('These are the available vaccines')
index = 1
for vc in range(4):
    print(index, VaccineInfo['Name'][vc], VaccineInfo['Price'][vc])
    index += 1 #index = index + 1

number = int(input('Please choose the vaccine No. between 1-4 : '))
while not number in range(1,5): #checking
    print('You can put only 1-4 :')
    number = int(input('Please choose the vaccine No. between 1-4 :')) #ask again
print('You choose', VaccineInfo['Name'][number-1])
print('Price is',  VaccineInfo['Price'][number-1])

#### Customer
check = 0 
listCustomer  = []
numCustomer = int(input('Please enter number of customer : '))
nameCustomer = input('Please enter your name:')
while True: 
    if nameCustomer.isalpha(): #if customer is alphabet
        listCustomer.append(nameCustomer)#append
        check +=1 #break
        if check == numCustomer:
            break
    else:  #number
        print('You can type only word')
    nameCustomer = input('Please enter your name:') #ask again
    
#### Result
# print(listCustomer)
print('-'*20)
print('Total Booking', len(listCustomer))
for idx, customer in enumerate(listCustomer):
    print(idx+1, customer)
print('Total Price', len(listCustomer) * VaccineInfo['Price'][number-1])
