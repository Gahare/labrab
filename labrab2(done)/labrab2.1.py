#расстояние между точками
import math

x1 = float(input("Введите х первой точки:"))
y1 = float(input("Введите у первой точки:"))
x2 = float(input("Введите х второй точки:"))
y2 = float(input("Введите у второй точки:"))
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(d)
