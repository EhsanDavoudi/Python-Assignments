names = []
name_ch = []
while True:
    name = input('Enter name(or Enter "stop" to close the program!): ')
    if name == 'stop':
        break
    else:
        names.append(name)
print(f'list of names: {names}\nthere is: ')
for name in names:
    cn = 0
    if name in name_ch:
        continue
    else:
        name_ch.append(name)
        for i in range(len(names)):
            if name == names[i]:
                cn += 1
    print(cn, name)