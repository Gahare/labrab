m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for j in range(n - 1):
    for i in range(n - 1):
        if a[i][0] > a[i + 1][0]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)
