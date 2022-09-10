#faghat baraye halate 2ta adad kar mikone
mpr = input('Enter your math problem: ')
mpr = mpr.split()
for op in range(len(mpr)):
    if mpr[op] == '*':
        op_og = mpr[op]
        first_num = int(mpr[op - 1])
        sec_num = int(mpr[op + 1])
        res = first_num * sec_num
    elif mpr[op] == '/':
        op_og = mpr[op]
        first_num = int(mpr[op - 1])
        sec_num = int(mpr[op + 1])
        res = first_num / sec_num
    elif mpr[op] == '+':
        op_og = mpr[op]
        first_num = int(mpr[op - 1])
        sec_num = int(mpr[op + 1])
        res = first_num + sec_num
    elif mpr[op] == '-':
        op_og = mpr[op]
        first_num = int(mpr[op - 1])
        sec_num = int(mpr[op + 1])
        res = first_num - sec_num
print(f'{first_num} {op_og} {sec_num} = {res}')