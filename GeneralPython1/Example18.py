#Dictionary
Pet = {
    #key,value
    #key => int float str
    #value => int float str boolean list tuple set
    'Bubi' : 'Dog',
    'Woody' : 'Bird',
    'ShooShoo' : 'Cat',
    100 : 'Fish',
    'Complex' : [0,1,2,3,4,5]
    }

print(Pet)
print(Pet['Bubi'])
Pet['Bubi'] = 'Elephant' #changable
print(Pet)
print(Pet[100])
print(Pet['Complex'][5]) #[finding value][index]
