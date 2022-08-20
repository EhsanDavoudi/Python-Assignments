import math

cn = int(input('How much do you want to use the calculator: '))
calc_type = input('what type do you want to use(Basic or Advanced): ')

if calc_type == 'Basic' or calc_type == 'basic':
    for i in range(cn):
        op = input('\nEnter the operator\n+ or sum, - or subtract \n/ or division, * or multiply: ')
        num1 = float(input('Enter number: '))
        num2 = float(input('Enter number: '))
        if op == '+' or op == 'sum':
            sum = num1 + num2
            print('\nsum of', num1, 'and', num2, ': ', sum)
        elif op == '-' or op == 'subtract':
            sub = num1 - num2
            print('\nsubtract of', num1, 'from', num2, ': ', sub)
        elif op == '/' or op == 'division':
            if num2 == 0:
                print('\na number cannot be divided by zero')
                continue
            else:
                div = num1 / num2
                print('\ndivision of', num1, 'by', num2, ': ', div)
        elif op == '*' or op == 'multiply':
            mul = num1 * num2
            print('\nmultiply of', num1, 'by', num2, ': ', mul)
        else:
            print('\nyour operator is not supported')
            continue
        print('\nyou used the calculator', i + 1)

elif calc_type == 'Advanced' or calc_type == 'advanced':
    for i in range(cn):
        op = input('\nEnter the operator from this List\n// or correctdivision, mod or remaining\n ^2 or power2, ^ or power\n | or absolutevalue, sin, cos, tan, cot\n √ or squareroot, primenumber: ')
        num1 = float(input('Enter number: '))
        if op == '^2' or op == 'power2' or op == '|' or op == 'absolutevalue' or op == 'sin' or op == 'cos' or op == 'tan' or op == 'cot' or op == '√' or op == 'squareroot' or op == 'primenumber':
            if op == '^2' or op == 'power2':
                power_2 = math.pow(num1,2)
                print('\n', num1, 'to power of 2: ', power_2)
            elif op == '|' or op == 'absolutevalue':
                av = math.fabs(num1)
                print('\nabsolute value of', num1, ': ', av)
            elif op == 'sin':
                sin = math.sin(num1)
                print('\nsine of', num1, ':', sin)
            elif op == 'cos':
                cos = math.cos(num1)
                print('\ncosine of', num1, ':', cos)
            elif op == 'tan':
                tan = math.tan(num1)
                print('\ntangent of', num1, ':', tan)
            elif op == 'cot':
                cot = math.atan(num1)
                print('\ntangent of', num1, ':', cot)
            elif op == '√' or op == 'squareroot':
                sr = math.sqrt(num1)
                print('\nsquare root of', num1, ':', sr)
            elif op == 'prime number':
                p_cn = 0
                for i in range(num1):
                    if num1 % i == 0:
                        cn += 1
                if cn == 2:
                    print('\n', num1, 'is a prime number')
                else:
                    print('\n', num1, 'is not a prime number')
        elif op == '//' or op == 'correctdivision' or op == 'mod' or op == 'remaining' or op == '^' or op == 'power':
            num2 = float(input('Enter number: '))
            if op == '//' or op == 'correctdivision':
                if num2 == 0:
                    print('\na number cannot be divided by zero')
                    continue
                else:
                    cd = num1 // num2
                    print('\ncorrect division of', num1, 'by', num2, ': ', cd)
            elif op == 'mod' or op == 'remaining':
                if num2 == 0:
                    print('\na number cannot be divided by zero')
                    continue
                else:
                    mod = num1 % num2
                    print('\nramaining of', num1, 'by', num2, ': ', mod)
            elif op == '^' or op == 'power':
                pow = math.pow(num1, num2)
                print('\n', num1, 'to power of',num2, ':', pow)
        else:
            print('\nyour operator is not supported')
            continue
        print('\nyou used the calculator', i + 1)
else:
    print('\nthis type is not supported')