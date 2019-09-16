a = float(input("Введите день:"))
b = float(input("Введите первый день года:"))
c = a % 7 + b
if 1 > a > 365 or 1 > b > 7:
    print("Некорректные данные")
if c == 0:
    c = 7
print(int(c), "день недели")
