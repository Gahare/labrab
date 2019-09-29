m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for i in range(n):
    linemax = max(a[i])
    linemin = min(a[i])
    print(linemin, linemax)
    for j in range(m):
        if a[i][j] == linemax:
            a[i][j] = linemin
        elif a[i][j] == linemin:
            a[i][j] = linemax
print(a)
