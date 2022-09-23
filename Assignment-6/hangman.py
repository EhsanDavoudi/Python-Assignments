import random

colors = ['red', 'blue', 'yellow', 'green', 'white', 'black']
animals = ['cow', 'sheep', 'goat', 'lion', 'wolf', 'cat']
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
used_alph = []
show_list = []

while True:
    cat = int(input('choose a category: \n1.color 2.animals '))
    if cat == 1:
        final_answer = random.choice(colors)
        break
    elif cat == 2:
        final_answer = random.choice(animals)
        break
    else:
        print('you have to Enter 1 or 2')
        continue

cn_w = len(final_answer)
cn_l = len(final_answer) + 2

for i in range(len(final_answer)):
    show_list.append(' _ ')
print(''.join(show_list))
while cn_l > 0 and cn_w > 0:
    user_letter = input('Enter a letter: ')
    user_letter = user_letter.lower()
    print(f'you have {cn_l} trys')
    if user_letter in alph:
        used_alph.append(alph.pop(alph.index(user_letter)))
        if user_letter in final_answer:
            for i in range(len(final_answer)):
                if final_answer[i] == user_letter:
                    show_list[i] = user_letter
                    cn_w -= 1 
        else:
            cn_l -= 1
        print(''.join(show_list))
        print(f'you can use this letters:\n{alph}')
        print(f'you already used this letters: {used_alph}')