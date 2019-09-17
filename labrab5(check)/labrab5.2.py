import math

a = float(input("Длина А:"))
b = float(input("Длина В:"))
if a <= b or a < 0 or b < 0:
    print("Некорректные данные")
print("Кол-во В в А:", math.floor(a / b))
