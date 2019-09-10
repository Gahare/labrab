# сумма разность произведение квадратов
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
if a == 0 or b == 0:
    print('Некорректные данные')
else:
    print(a * a + b * b)
    print(a * a - b * b)
    print((a * a) * (b * b))
    print(round((a * a) / (b * b), 5))
