end_counter = 0
while end_counter != 1: 
    first_temp = input('vahed dama ra vared konid az bein "F", "C", "K": ')
    sec_temp = input('vahed damaye ke mikhahid tabdil shavad ra vared konid az bein "F", "C", "K":')
    if ((first_temp == 'F') or (first_temp == 'C') or (first_temp == 'K')) and ((sec_temp == 'F') or (sec_temp == 'C') or (sec_temp == 'K')) and first_temp != sec_temp:
        temp = int(input('dama ra vared konid: '))
        end_counter = 1
    else:
        print('vahed dama bayad az bein "F", "C", "K" bashad')

if first_temp == 'C':
    if sec_temp == 'F':
        temp = (temp * 9.5) + 32
        print('dama be farenheit: ', temp)
    elif sec_temp == 'K':
        temp = (temp + 273.15)
        print('dama be kelvin: ', temp)
elif first_temp == 'F':
    if sec_temp == 'C':
        temp = (temp - 32) / 9.5
        print('dama be celsius: ', temp)
    elif sec_temp == 'K':
        temp = 1.8 / (temp + 459.67)
        print('dama be kelvin: ', temp)
elif first_temp == 'K':
    if sec_temp == 'C':
        temp = (temp + 273.15)
        print('dama be celsius: ', temp)
    elif sec_temp == 'F':
        temp = 459.67 - (temp * 1.8)
        print('dama be farenheit: ', temp)