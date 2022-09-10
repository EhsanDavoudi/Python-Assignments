sen = input('Enter your phrase: ')
splitter = input('Enter a word: ')
sticker = input('Enter another word: ')

sen = sen.split(splitter)
sen = sticker.join(sen)
print(f'\nyour new phrase: {sen}')