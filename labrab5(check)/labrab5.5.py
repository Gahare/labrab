a = int(input("Введите число:"))
sot = a // 100
a = a - sot * 100
dec = a // 10
un = a % 10
print(dec * 100 + un * 10 + sot)
