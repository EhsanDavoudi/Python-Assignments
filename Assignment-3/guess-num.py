import random
s_num = 0
b_num = 99
num = random.randint(s_num, b_num)
while True:
    print('is it', num, '? (Yes/No)')
    ans = input()
    if ans == 'Yes' or ans == 'yes':
        print('yay i won')
        break
    elif ans == 'No' or ans == 'no':
        pos = input('is it bigger or smaller: ')
        if pos == 'bigger':
            s_num = num + 1
            num = random.randint(s_num, b_num)
        elif pos == 'smaller':
            b_num = num - 1
            num = random.randint(s_num, b_num)
        else:
            print('answer should bigger or smaller')
            continue
    
    else:
        print('answer should be between yes or no')
        continue