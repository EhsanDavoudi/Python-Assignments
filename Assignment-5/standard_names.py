names = []
for i in range(10):
    name = input('give me a name: ')
    name = name.lower()
    first = name[0]
    up = first.upper()
    name = name.replace(name[0], up, 1)
    names.append(name)
print(names)