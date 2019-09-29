m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
minstolb = 0
maxstolb = 0
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
listmax = a[0][0]
listmin = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > listmax:
            listmax = a[i][j]
            maxstolb = j
        if a[i][j] < listmin:
            listmin = a[i][j]
            minstolb = j
for i in range(n):
    a[i][maxstolb], a[i][minstolb] = a[i][minstolb], a[i][maxstolb]
print(a)
print(listmax, listmin)
