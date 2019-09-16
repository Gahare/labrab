import math

a = float(input("Длина А:"))
b = float(input("Длина В:"))
if a <= b or a < 0 or b < 0:
    print("Некорректные данные")
print("Незанятая часть А:", a - math.floor(a / b) * b)
