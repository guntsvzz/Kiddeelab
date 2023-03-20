#dictionary method

resume = {
    #key        : Value
    'Name'      : 'Gun',
    'Height'    : 174,
    'Weight'    : 65,
    'Blood'     : 'O',
    'Workplace' : 'Lasalle'
}

#keys
print(resume.keys())
#values
print(resume.values())
print(resume['Name']) 
#get
print(resume.get('Name'))
#update
resume.update({'Age':23})
print(resume)