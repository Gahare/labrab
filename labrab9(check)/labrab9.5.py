a = int(input())
print('год', end=' ')
a = a - 1983
while a > 60:
    a = a - 60
if a < 13: b = 0
if 12 < a < 25: b = 1
if 24 < a < 37: b = 2
if 36 < a < 49: b = 3
if 48 < a < 61: b = 4

if b == 0:
    print('зелен', end='')
if b == 1:
    print('красн', end='')
if b == 2:
    print('желт', end='')
if b == 3:
    print('бел', end='')
if b == 4:
    print('черн', end='')

c = a % 12
if c == 3 or c == 4 or c == 5:
    print('ого', end=' ')
else:
    print('ой', end=' ')

if c == 1:
    print('крысы')
if c == 2:
    print('коровы')
if c == 3:
    print('тигра')
if c == 4:
    print('зайца')
if c == 5:
    print('дракона')
if c == 6:
    print('змеи')
if c == 7:
    print('лошади')
if c == 8:
    print('овцы')
if c == 9:
    print('собезьяны')
if c == 10:
    print('курицы')
if c == 11:
    print('собаки')
if c == 0:
    print('свиньи')
