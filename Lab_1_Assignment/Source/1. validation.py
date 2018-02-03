import re               #importing regular expressions to allow special characters
while True:             #Using a while loop to validate the required password
    p = input('\nEnter a valid password:')               #Entering password
    if(len(p) < 6 or len(p) > 16):                       #Using IF loop conditions to determine the correct Password
     print('Password must be between 6 and 16 characters.')
    elif re.search('[0-9]',p) is None:
     print('Password must have atleast one number')
    elif re.search('[$,@,!,*]',p) is None:
     print('Password must have one special character')
    elif re.search('[A-Z]',p) is None:
     print('Password must have one upper case character')
    elif re.search('[a-z]',p) is None:
     print('Password must have one lower case character')
    else :
     print('\nPassword accepted')
     break                        #using break in order to avoid infinite loop

