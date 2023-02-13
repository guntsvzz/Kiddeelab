name  = input('Enter name :') #string
score = float(input('Enter score out of 120:'))

#return percentage
def percentage(score):
    maximum = 120
    percent = (score/maximum) * 100
    return round(percent, 2)

print(name,'got percentage', percentage(score),'%')