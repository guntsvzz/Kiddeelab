day = input('Enter day:')
time = input('Enter time:')
days = {
    #key:value
    "Monday"    : {
        "07:25-08:10" : "Value",
        "08:35-09:20" : "LA",
        "09:20-10:10" : "Science",
        "10:10-11:00" : "Thai",
        "12:00-12:50" : "Math",
        "12:50-13:30" : "PE",
        "13:30-14:20" : "RA"
    },
    "Tuesday"   : {}
    
}

print(days[day][time])