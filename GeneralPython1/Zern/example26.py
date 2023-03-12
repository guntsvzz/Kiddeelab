#string
sentence = 'hello world'
#str.function/method()
###Count Method
print(sentence.count('l')) #alphabet
print(sentence.count('L')) #case sensitive
print(sentence.count('hello')) #word

###Replace Method
#replace(old,new)
print(sentence.replace('o','a'))
print(sentence.replace(' ','-'))

###Split Method
#split(?) str -> list
new = sentence.split(' ') #list
print(new)
print(new[0])
print(new[1])

###Upper method
print(sentence.upper())
###Lower method
print(sentence.lower())
###Capitalize method
print(sentence.capitalize())

###isalpha check that is all string items alphabet
print(sentence)
print(sentence.isalpha())
sentence2 = 'helloworld'
print(sentence2.isalpha())
###isdigit
print(sentence.isdigit())
s1 = '123'
s2 = 'h123'
s3 = '123h'
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())

story = 'On shewing this to Dr. Johnson, he said, “Sir, you have straightened out the Feet,\
    but you have put neither Wit nor Poetry into the Lines.” \
    It wou’d afford me Gratification to tell more of my Experiences with \
    Dr. Johnson and his circle of Wits; but I am an old Man, and easily fatigued. I seem\
    to ramble along without much Logick or Continuity when I endeavour to recall the Past; and fear\
    I light upon but few Incidents which others have not before discuss’d. Shou’d my\
    present Recollections meet with Favour, I might later set down some further Anecdotes of old\
    Times of which I am the only Survivor. I recall many things of Sam Johnson and his Club,\
    having kept up my Membership in the Latter long after the Doctor’s Death, at which I sincerely\
    mourn’d. I remember how John Burgoyne, Esq., the General, whose Dramatick and Poetical\
    Works were printed after his Death, was blackballed by three Votes; probably because of his\
    unfortunate Defeat in the American War, at Saratoga. Poor John! \
    His Son fared better, I think, and was made a Baronet. But I am very tired. \
    I am old, very old, and it is Time for my Afternoon Nap.'

#counting he she it
ask = input('Do u want to stop this class(Yes/No)')
if ask.isalpha():
    if ask[0].lower() == 'y':
        print('OK take a break')
    elif ask[0].lower() == 'n':
        print('Fine continue')
    else:
        print('You can only type yes/no')
elif ask.isdigit():
    print('Wrong, u cannot type number')

