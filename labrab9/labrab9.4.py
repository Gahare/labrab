a1 = input()
a = int(a1[0])
b = int(a1[1])
c = int(a1[2])


def dec(a, c):
    if a == 2:
        print('двадцать', end=' ')
    if a == 3:
        print('тридцать', end=' ')
    if a == 4:
        print('сорок', end=' ')
    if a == 5:
        print('пятьдесят', end=' ')
    if a == 6:
        print('шестьдесят', end=' ')
    if a == 7:
        print('семьдесят', end=' ')
    if a == 8:
        print('восемдесят', end=' ')
    if a == 9:
        print('девяносто', end=' ')
    odin(c)


def odin(a):
    if a == 1:
        print('один', end=' ')
    if a == 2:
        print('два', end=' ')
    if a == 3:
        print('три', end=' ')
    if a == 4:
        print('четыре', end=' ')
    if a == 5:
        print('пять', end=' ')
    if a == 6:
        print('шесть', end=' ')
    if a == 7:
        print('семь', end=' ')
    if a == 8:
        print('восемь', end=' ')
    if a == 9:
        print('девять', end=' ')


def iskl(b, c):
    f = str(b) + str(c)
    f = int(f)
    if f == 10:
        print('десять', end=' ')
    if f == 11:
        print('одиннадцать', end=' ')
    if f == 12:
        print('двенадцать', end=' ')
    if f == 13:
        print('тринадцать', end=' ')
    if f == 14:
        print('четырнадцать', end=' ')
    if f == 15:
        print('пятнадцать', end=' ')
    if f == 16:
        print('шестнадцать', end=' ')
    if f == 17:
        print('семнадцать', end=' ')
    if f == 18:
        print('восемнадцать', end=' ')
    if f == 19:
        print('девятнадцать', end=' ')


if a == 1:
    print('сто', end=' ')
if a == 2:
    print('двести', end=' ')
if a == 3:
    print('триста', end=' ')
if a == 4:
    print('четыреста', end=' ')
if a == 5:
    print('пятьсот', end=' ')
if a == 6:
    print('шестьсот', end=' ')
if a == 7:
    print('седьмьсот', end=' ')
if a == 8:
    print('восьмьсот', end=' ')
if a == 9:
    print('девятьсот', end=' ')
if b == 1:
    iskl(b, c)
else:
    dec(b, c)
