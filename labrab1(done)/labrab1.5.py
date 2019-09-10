# сумма разность произведние модулей
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
if a == 0 or b == 0:
    print('некорректные данные')
else:
    print(abs(a) + abs(b))
    print(abs(a) - abs(b))
    print(abs(a) * abs(b))
    print(round(abs(a) / abs(b), 5))
