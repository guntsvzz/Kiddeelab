#Method List
# ls = [1, 2, 7, 0 , -5]
# print(ls)
# #append = add
# ls.append(5) 
# print(ls)
# #remove
# ls.remove(2)
# print(ls)
# ls.sort() #less to more
# print(ls) 
# ls.sort(reverse=True) #more to less
# print(ls)

list_odd = []
list_even = []
print('Before')
print(list_odd)
print(list_even)

for number in range(11):
    # print(number)
    if number%2 == 1: #odd
        list_odd.append(number)
    if number%2 == 0: #even
        list_even.append(number)

print('After')
print(list_odd)
print(list_even)