set1 = {'1','2','3','4'}
set2 = {'2','4','5','7'}
print(set1)
print(set2)

#remove
set1.remove('1')
print(set1)
#update
set1.update('1')
print(set1)
#intersecrtion
inter = set1.intersection(set2) #set2.intersection(set1)
print(inter)