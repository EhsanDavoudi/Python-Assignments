num = int(input('adadi vared konid: '))

rev_num = 0
num1 = num

while num1 != 0:
    rev_num = num1 % 10 + (10 * rev_num) 
    num1 //= 10    
if num == rev_num: 
    print('adad shoma ba makus aan barabar ast')
else:
    print('adad shoma ba makus aan barabr nist')