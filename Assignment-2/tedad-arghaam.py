num = int(input('adadi sahih vared konid: '))

end_counter = 0
f_counter = 0
z_counter = 0 
while end_counter != 1:
    num1 = num % 10
    num //= 10
    if num1 % 2 == 0:
        z_counter += 1
    elif num1 % 2 != 0:      
        f_counter += 1
    if num == 0:
        if f_counter > z_counter:
            print('tedad argham fard bishtar ast')
        elif z_counter > f_counter:
            print('tedad argham zoj bishtar ast')
        elif z_counter == f_counter:
            print('tedad argham zoj o fard barabar ast')
        end_counter = 1