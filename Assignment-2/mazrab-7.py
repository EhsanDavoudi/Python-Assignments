num = int(input('adadi vared konid: '))

if num % 7 == 0:
    print('adad shoma mazrab 7 ast')
else:
    while num % 7 != 0:
        num += 1
    print('mazrab 7 baadi: ', num)