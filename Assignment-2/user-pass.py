username = 'ehsan'
password = 'ehsan1234'

counter = 1
while counter < 4:
    un = input('username ra vared konid: ')
    pw = input('password ra vared konid: ')
    if un == username and pw == password:
        print('mitavanid vared shavid')
        counter += 2
    elif counter == 3:
        print('account shoma ghofl shod')
    else:
        print('dobare talash konid')
    counter += 1