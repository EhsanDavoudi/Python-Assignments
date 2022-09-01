numbers = []
sort = True
for i in range(0, 10):
    num = int(input('Enter a number: '))
    numbers.append(num)
for number in range(1, len(numbers)):
    if numbers[number -1] < numbers[number] or numbers[-number] < numbers[-number - 1]:
        sort = True
    else:
        sort = False
        break
if sort == True:
    print('Yes!')
else:
    print('No!')