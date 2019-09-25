m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for i in range(n // 2):
    for j in range(m // 2):
        a[i][j], a[i + n // 2][j + m // 2] = a[i + n // 2][j + m // 2], a[i][j]
print(a)
