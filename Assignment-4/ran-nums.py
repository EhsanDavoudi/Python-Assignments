import random
nums = int(input('How many random numbers you want: '))
numbers = []
sort = True
for i in range(0, nums):
    num = random.randint(0, nums * 10)
    numbers.append(num)
for number in range(0, len(numbers) - 1):
    if numbers[number] == numbers[:]:
        numbers.pop(number)
print('list of', nums , 'random numbers:', numbers)