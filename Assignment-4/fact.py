num = int(input('Enter a Number: '))
total = 1
cn = 1
while True:
    total *= cn
    if total == num:
        print(num, 'is factorial of', cn)
        break
    elif total > num:
        print(num, 'is not factorial of any number')    
        break
    cn += 1