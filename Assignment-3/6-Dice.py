import random
sum = 0
while True:
    num = random.randint(1,6)
    sum += num
    if num == 6:
        continue
    else:
        break
print('Total:', sum)