Contactslist = [{'Name': 'huzaifa', 'Number': '8745632140', 'email': 'hh@ymail.com'},
                {'Name': 'hussain', 'Number': '9632147850', 'email': 'ss@ymail.com'}]
while True:
    print('\nGive your choice:')
    print('1. Display contact by name')
    print('2. Display contact by number')
    print('3. Edit contact by name')
    print('4. Exit')
    Input_choice = int(input('\nPlease enter one choice from above :'))
    if Input_choice == 1:
        print('\nThe Contacts Names are :')
        for y in Contactslist:
            x = 0
            while (x < 1):
                names = y['Name']
                print(names)
                x += 1
        break

    elif Input_choice == 2:
        print('\nThe Contacts Numbers are :')
        for m in Contactslist:
            n = 0
            while (n < 1):
                numbers = m['Number']
                print(numbers)
                n += 1
        break

    elif Input_choice == 3:
        print('\nthe contacts list details are :\n', Contactslist)
        Edit_number = input('\nProvide name to modify the phone number:')
        New_number = input('\nNow provide the New phone number:')
        for z in Contactslist:
            if z['Name'] in Edit_number:
                z['Number'] = New_number
                print('\nUpdated contacts list is \n', Contactslist)
        break

    elif Input_choice == 4:
        print('\nExit done')
        break

    else:
        print('something went wrong, please provide valid choice')
        continue
