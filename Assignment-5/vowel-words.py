words = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
sen = input('give me a word: ')
for i in sen:
    if i in words:
        sen = sen.replace(i, "?")
print(sen)