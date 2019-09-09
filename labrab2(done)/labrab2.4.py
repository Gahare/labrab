#периметр площадь прямоугольника по 2 точкам
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
h = abs(y2 - y1)
w = abs(x2 - x1)
print(h * w)
print(h * 2 + w * 2)
