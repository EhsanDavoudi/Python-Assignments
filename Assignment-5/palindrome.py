phr = input('Enter your phrase: ')

cn = len(phr) - 1
pal_check = True

for i in range(len(phr) - 1):
    if phr[i] == phr[cn]:
        pal_check = True
        cn -= 1
    else:
        pal_check = False
if pal_check == True:
    print('your phrase is palindrome')
else:
    print('your phrase is not palindrome')