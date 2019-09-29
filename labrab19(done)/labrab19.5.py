m = int(input())  # vniz
a = [0] * m
sum = 0
for i in range(m):
    a[i] = [0] * m
for i in range(m):
    for j in range(m):
        a[i][j] = float(input())
for i in range(1, m):
    w = i
    for z in range(m - i):
        sum = sum + a[w][z]
        w = w + 1
for i in range(1, m):
    w = i
    for z in range(m - i):
        sum = sum + a[z][w]
        w = w + 1
print(sum)
