def odin(z):
    if z == 1:
        print('одно учебное задание', end=' ')
    if z == 2:
        print('два учебных задания', end=' ')
    if z == 3:
        print('три учебных задания', end=' ')
    if z == 4:
        print('четыре учебных задания', end=' ')
    if z == 5:
        print('пять учебных заданий', end=' ')
    if z == 6:
        print('шесть учебных заданий', end=' ')
    if z == 7:
        print('семь учебных заданий', end=' ')
    if z == 8:
        print('восемь учебных заданий', end=' ')
    if z == 9:
        print('девять учебных заданий', end=' ')


a = int(input())
if a < 10:
    odin(a)

if 9 < a < 21 or a == 20 or a == 30 or a == 40:
    if a == 10:
        print('десять', end=' ')
    if a == 11:
        print('одиннадцать', end=' ')
    if a == 12:
        print('двенадцать', end=' ')
    if a == 13:
        print('тринадцать', end=' ')
    if a == 14:
        print('четырнадцать', end=' ')
    if a == 15:
        print('пятнадцать', end=' ')
    if a == 16:
        print('шестнадцать', end=' ')
    if a == 17:
        print('семнадцать', end=' ')
    if a == 18:
        print('восемнадцать', end=' ')
    if a == 19:
        print('девятнадцать', end=' ')
    if a == 20:
        print('двадцать', end=' ')
    if a == 30:
        print('тридцать', end=' ')
    if a == 40:
        print('сорок', end=' ')
    print('учебных заданий')
if 20 < a < 30:
    print('двадцать', end=' ')
    odin(a - 20)
if 30 < a < 40:
    print('тридцать', end=' ')
    odin(a - 30)
