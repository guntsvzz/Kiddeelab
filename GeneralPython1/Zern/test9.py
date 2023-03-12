times = int(input('How many time? ')) #3

for i in range(times): 
    print('No.', i+1)
    char = ['x','*','#']
    symbol = int(input('Enter the value:'))
    for j in range(symbol):
        print(char[i%3],end=' ')
    print()

#HW symbol x * #
# x 1,4,7,...
# * 2,5,8,...
# # 3,6,9,...
# %%
print(4%4)
# %%
