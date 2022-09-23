def shape(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0):
                print('$', end='')
            else:
                print('&', end='')
        print()

n = int(input('Enter a number: '))
m = int(input('Enter a number: '))

shape(n, m)