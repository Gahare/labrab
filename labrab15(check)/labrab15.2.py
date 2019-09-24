import random
n = int(input())
a = []
b = []
suma = 0
for i in range(n):
    a.append(random.uniform(-100, 100))
for i in range(n):
    suma = suma + a[i]
    b.append(suma / (i + 1))
print(b)
