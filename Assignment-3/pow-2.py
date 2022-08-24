import math
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num_2 = []

for i in range(len(num)):
    num_2.append(math.pow(num[i], 2))

print('Numbers from 1 to 20: ', num)
print('Numbers from 1 to 20 to power of two: ' ,num_2)