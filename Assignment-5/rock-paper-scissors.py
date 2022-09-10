import random

cn_p = 0
cn_pc = 0
cn_p1 = 0
cn_p2 = 0

while True:
    tp = int(input('1.single player\n2.multiplayer\nchoose the type of the game(1 or 2): '))
    sett = int(input('how many times you want to play?\nchoose between "1", "3" or "5": '))
    if (sett == 1 or sett == 3 or sett == 5) and (tp == 1 or tp == 2):
        while (sett > cn_p and sett > cn_pc) and (sett > cn_p1 and sett > cn_p2):
            if tp == 1:
                ans = input('rock, paper, scissors? ')
                if ans == 'rock' or ans == 'paper' or ans == 'scissors':
                    ch = ['rock', 'paper', 'scissors']
                    pc_ch = random.choice(ch)
                    print(f'i say {pc_ch}')
                    if (ans == 'rock' and pc_ch == 'scissors') or (ans == 'scissors' and pc_ch == 'paper') or (ans == 'paper' and pc_ch == 'rock'):
                        print(cn_p)
                    elif (ans == 'rock' and pc_ch == 'paper') or (ans == 'scissors' and pc_ch == 'rock') or (ans == 'paper' and pc_ch == 'scissors'):
                        print(cn_pc)
                    else:
                        cn_p += 1
                        cn_pc += 1
                else:
                    print('your answer should be "rock" or "paper" or "scissors"')
                    continue
            elif tp == 2:
                ans_p1 = input('rock, paper, scissors?\nPlayer1: ')
                ans_p2 = input('Player2: ')
                if (ans_p1 == 'rock' or ans_p1 == 'paper' or ans_p1 == 'scissors') and (ans_p2 == 'rock' or ans_p2 == 'paper' or ans_p2 == 'scissors'):
                    if (ans_p1 == 'rock' and ans_p2 == 'scissors') or (ans_p1 == 'scissors' and ans_p2 == 'paper') or (ans_p1 == 'paper' and ans_p2 == 'rock'):
                        cn_p1 += 1
                    elif (ans_p1 == 'rock' and ans_p2 == 'paper') or (ans_p1 == 'scissors' and ans_p2 == 'rock') or (ans_p1 == 'paper' and ans_p2 == 'scissors'):
                        cn_p2 += 1
                    else:
                        cn_p1 += 1 
                        cn_p2 += 1
                else:
                    print('your answer should be "rock" or "paper" or "scissors"')
                    continue
        break
    elif (tp != 1 or tp != 2) and (sett == 1 or sett == 3 or sett == 5):
        print('type of the game should be between "1" or "2"')
        continue
    elif(tp == 1 or tp == 2) and (sett != 1 or sett != 3 or sett != 5):
        print('times you want to play has to be between "1", "3" or "5"')
        continue
    else:
        print('You have entered something wrong\ntry again')
if tp == 1:
    if cn_p == sett and cn_p != cn_pc:
        print('you won')
    elif cn_pc == sett and cn_pc != cn_p:
        print('you lost')
    elif cn_p == cn_pc:
        print('draw')
elif tp == 2:
    if cn_p1 == sett and cn_p1 != cn_p2:
        print('Player1 won and Player2 lost')
    elif cn_p2 == sett and cn_p1 != cn_p2:
        print('Player2 won and Player1 lost')
    elif cn_p1 == cn_p2:
        print('draw')