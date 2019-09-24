m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
k = int(input())
sum = 0
proiz = 1
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for j in range(m):
    sum = sum + a[k - 1][j]
    proiz = proiz * a[k - 1][j]
print(sum)
print(proiz)
