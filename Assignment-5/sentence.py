sen = input('give me a sentence: ')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lt_lis = []
ch_cn = 0
wd_lis = sen.split()
for i in letters:
    lt = sen.count(i)
    if lt > 0:
        lt_lis.append(f'{lt} {i}')
for i in wd_lis:
    ch_cn += len(i)
for i in sen:
    sp_cn = sen.count(' ')
    ent_cn = sen.count('\n')
    per_cn = sen.count('.')
    com_cn = sen.count(',')
print(f'number of letters: {lt_lis}\nnumber of words: {len(wd_lis)}\nnumber of charachters: {ch_cn}\nnumber of spaces: {sp_cn} and enters: {ent_cn}\nnumber of periods: {per_cn} and commas: {com_cn}')