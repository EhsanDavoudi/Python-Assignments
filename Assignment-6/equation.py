import math
def eq(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c 
    if delta > 0:
        first_root =  (-b + math.sqrt(delta)) / (2 * a)
        sec_root =  (-b - math.sqrt(delta)) / (2 * a)
        print(f'roots of the equation are: {first_root} and {sec_root}')
    elif delta == 0:
        root = -b / (2 * a)
        print(f'root of the equation is: {root}')
    else:
        print('equation has no roots')

a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c: '))
eq(a, b, c)