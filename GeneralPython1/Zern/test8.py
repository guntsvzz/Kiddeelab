day = input('Enter day:')
days = {
    #key:value
    "Monday"    :'09:00 AM - 10:30 AM',
    "Tuesday"   :'11:00 AM - 12:30 AM',
    'Tuesday'   :'11:00 AM - 12:30 AM',
    'Wednesday' :'08:30 AM - 10:00 AM',
    'Thursday'  :'11:30 AM - 01:30 PM',
    'Friday'    :'02.00 PM - 03.30 PM'
}
print('You have',days[day],'on',day)