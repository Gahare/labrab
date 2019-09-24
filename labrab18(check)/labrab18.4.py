m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
b = []
sum = 0
num = 0
count = 0
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
for i in range(m):
    for j in range(n):
        sum = sum + a[j][i]
        num = num + 1
    b.append(sum / num)
    sum = 0
    num = 0
for i in range(m):
    for j in range(n):
        if a[j][i] > b[i]:
            count = count + 1
    print(i + 1, "stolbec", count)
    count = 0
