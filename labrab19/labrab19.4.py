m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
firstmas = []
curmas = []
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for i in range(n):
    firstmas.append(a[i][0])
