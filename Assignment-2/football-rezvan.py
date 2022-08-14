counter = 1
win = 0
draw = 0
lose = 0
points = 0

while counter <= 8:
    print('emtiaz match', counter, 'ra vared konid: ')
    res = int(input())
    if res == 3:
        win += 1
        counter += 1
        points += res
    elif res == 1:
        draw += 1
        counter += 1
        points += res
    elif res == 0:
        lose += 1
        counter += 1
    else:
        print('emtiaz bayad bein 0, 1 ya 3 bashad (0 baraye bakht, 1 baraye mosavi va 3 baraye bord)')
print('emtiaz nahayi team: ', points)
print('tedad bord: ', win)
print('tedad bakht: ', lose)
print('tedad mosavi: ', draw)