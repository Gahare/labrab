import math
x1 = int(input("Введите х первой точки:"))
y1 = int(input("Введите у первой точки:"))
x2 = int(input("Введите х второй точки:"))
y2 = int(input("Введите у второй точки:"))
d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(d)
