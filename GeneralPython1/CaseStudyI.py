print('Type the number to choose the vaccine')
vaccine = {
    'name' : ['Pfizer','Moderna','Sinopharm','Sinovac'],
    'price' : [3000,3300,3400,0]
    }
for i in range(4): #0,4,1
    print(i+1,':',vaccine['name'][i])
#asking vaccine
choice = int(input('Choose a choice for Vaccine:'))
while not(choice > 0 and choice < 5):
    print('Please type 1,2,3 or 4')
    choice = int(input('Choose a choice for Vaccine:'))
print('You choose',vaccine['name'][choice-1])
customer_list = []
#amount of customer 
print('Please insert customer\'s name:')
customer = input('Name:')
while (customer != ''): 
    if customer.isalpha():
        customer_list.append(customer)
        customer = input('Name:')     
    else:
        print('Please enter customer name only')
        customer = input('Name:')
#result
print('Total number of booking vaccination:',len(customer_list))
print('Total price:', len(customer_list)*vaccine['price'][choice-1]) #totalpeople*price
print('Customer Name List:')
for i in range(len(customer_list)):
    print(i+1,customer_list[i])


