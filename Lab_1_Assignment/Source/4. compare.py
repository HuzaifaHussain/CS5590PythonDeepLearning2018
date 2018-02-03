list_python = ['zia','huzaifa','faraz','asif','sohail','mujtaba']
list_webapp = ['zia','huzaifa','gani','faheem','mujtaba','zeeshan']
same = []               #making empty strings first
not_same = []
for x in list_python:     # checking students in python list

    if x in list_webapp:      #if they're in webapp class also then append in 'same' string
        same.append(x)

    else:
        not_same.append(x)  # or else append into another string

for y in list_webapp:
    if y not in list_python:
        not_same.append(y)
print('Students who take both Python and Web Application are: ')
print('\n'.join(same))                #\n is for next line
print('\nStudents who are Not Common in Python And Web Application are:')
print('\n'.join(not_same))