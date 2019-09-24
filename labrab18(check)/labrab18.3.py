m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
b = []
proiz = 1
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for i in range(m):
    for j in range(n):
        proiz = proiz * a[j][i]
    b.append(proiz)
minim = min(b)
num = b.index(minim)
print(num + 1)
print(minim)
