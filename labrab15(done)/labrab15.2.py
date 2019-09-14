n = int(input())
a = []
b = []
suma = 0
for i in range(n):
    a.append(float(input()))
for i in range(n):
    suma = suma + a[i]
    b.append(suma / (i + 1))
print(b)
