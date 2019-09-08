# должен быть способ проще
def odin(a):
    if a == 1:
        print('первое', end=' ')
    if a == 2:
        print('второе', end=' ')
    if a == 3:
        print('третье', end=' ')
    if a == 4:
        print('четвертое', end=' ')
    if a == 5:
        print('пятое', end=' ')
    if a == 6:
        print('шестое', end=' ')
    if a == 7:
        print('седьмое', end=' ')
    if a == 8:
        print('восьмое', end=' ')
    if a == 9:
        print('девятое', end=' ')


a = int(input())
b = int(input())

if a > 9:
    if a == 10:
        print('десятое', end=' ')
    if a == 11:
        print('одиннадцатое', end=' ')
    if a == 12:
        print('двенадцатое', end=' ')
    if a == 13:
        print('тринадцатое', end=' ')
    if a == 14:
        print('четырнадцатое', end=' ')
    if a == 15:
        print('пятнадцатое', end=' ')
    if a == 16:
        print('шестнадцатое', end=' ')
    if a == 17:
        print('семнадцатое', end=' ')
    if a == 18:
        print('восемнадцатое', end=' ')
    if a == 19:
        print('девятнадцатое', end=' ')
    if a == 20:
        print('двадцатое', end=' ')
    if 20 < a < 30:
        a = a % 20
        print('двадцать', end=' ')
        odin(a)
    if a == 30:
        print('тридцатое', end=' ')
    if a > 30:
        a = a % 30
        print('тридцать', end=' ')
        odin(a)
else:
    odin(a)

if b == 1:
    print('января')
if b == 2:
    print('февраля')
if b == 3:
    print('марта')
if b == 4:
    print('апреля')
if b == 5:
    print('мая')
if b == 6:
    print('июня')
if b == 7:
    print('июля')
if b == 8:
    print('августа')
if b == 9:
    print('сентября')
if b == 10:
    print('октября')
if b == 11:
    print('ноября')
if b == 12:
    print('декабря')
