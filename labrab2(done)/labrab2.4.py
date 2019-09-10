# периметр площадь прямоугольника по 2 точкам
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
h = abs(y2 - y1)
w = abs(x2 - x1)
print(h * w)
print(h * 2 + w * 2)
