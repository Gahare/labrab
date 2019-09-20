a = float(input())
if a == 0:
    print('Нулевое число')
else:
    if a % 2 == 0:
        print('Четное', end=' ')
    else:
        print('Нечетное', end=' ')
    if a < 0:
        print('отрицательное число')
    else:
        print('положительное число')
