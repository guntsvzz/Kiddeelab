elephant = 'elephant'
ant = 'ant'
cat = 'cat'
# %%
zoo1 = ['tiger','elephant','snake'] #list
zoo2 = ('tiger','elephant','snake') #tuple
zoo3 = {'tiger','elephant','snake'} #set
#set doesn't have an order
print(zoo1)
print(zoo2)
print(zoo3)
# %%
#index <==> order
print(zoo1[1]) #list
print(zoo2[2]) #tuple
# %%
#list is able to change any item but tuple cannot 
zoo1[0] = 'bird' #change tiger to bird
print(zoo1)
#conclusion 
#tuple is fast
#list changable item
#set is unique

# %%
number = [1,2,3,4,6,1,2,3,5,7,9,0,1,2,3,4]
print(set(number)) #return unique value 
# %%
zoo = ['tiger','elephant','snake']
number = [1,2,3]
#1st
zoo_list = [
    ['tiger',1],['elephant',2],['snake',3]
]
print(zoo_list[1][0])
# %%
#2nd
#dictionary
zoo_dict = {
    #key:Value
    'tiger': 1,
    'elephant': 2,
    'snake':3
}
print(zoo_dict['tiger'])
# %%
