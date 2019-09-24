import math

a = []
xmax = 0
ymax = 0
distance = 0
for i in range(int(input()) * 2):
    a.append(float(input()))
for i in range(0, len(a), 2):
    if a[i] < 0 and a[i + 1] > 0:
        curdistance = math.sqrt(a[i] ** 2 + a[i + 1] ** 2)
        if curdistance > distance:
            distance = curdistance
            xmax = a[i]
            ymax = a[i + 1]
print(xmax, ymax)
