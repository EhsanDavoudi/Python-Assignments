password = 1234
wrong_pass = 4321
counter = 1

while True:
    passw = int(input('Enter password: '))

    if counter == 3:
        print('your account is locked')
        break
    
    if passw == password:
        print('you are logged in')
        break
    elif passw == wrong_pass:
        print('bye👋\nhave a good time with cops')
        break
    elif passw <= 1000 or passw >= 9999:
        print('password cant be less or more than 4 digits')
    else:
        print('try again')
        counter += 1