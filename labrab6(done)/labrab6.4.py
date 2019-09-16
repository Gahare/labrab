a = float(input("Ширина прямоугольника:"))
b = float(input("Длина прямоугольника:"))
c = float(input("Сторона квадрата:"))
if a <= 0 or b <= 0 or c <= 0:
    print()
ac = a // c
bc = b // c
print("Кол-во квадратов -", ac * bc)
print("Остаток площади -", a * b - ac * bc * c * c)
