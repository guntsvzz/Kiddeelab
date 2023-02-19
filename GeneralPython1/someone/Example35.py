#Set
set1 = {'1', '5', '7', '8' , '2', '5', '9'}
set2 = {'2', '7', '4'}
print(set1)
print(set2)
#remove method
set1.remove('5')
print(set1)
#updatess
set2.update('6')
print(set2)
#difference
print(set1.difference(set2))
print(set2.difference(set1))
#intersection
print(set1.intersection(set2))
