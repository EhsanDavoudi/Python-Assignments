weight = float(input('vazn ra be kilogram vared konid: '))
height = float(input('ghad khode ra  be metr vared konid: '))

bmi = weight / (height ** 2)
if 16 > bmi:
    print('vazn o ghad shoma tabii nist')
elif 16 < bmi <= 18.5:
    print('shoma moshkel kahesh vazn darid')
elif 18.5 < bmi <= 24:
    print('vazn shoma ideal ast')
elif 24 < bmi <= 30:
    print('shoma kami ezafe vazn darid')
elif 30 < bmi <= 35:
    print('shoma ezafe vazn darid')
elif 35 < bmi <= 40:
    print('shoma meghdar ziadi ezafe vazn darid')
elif 40 < bmi:
    print('shoma bish az had ezafe vazn darid')
