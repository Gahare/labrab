n = int(input())
m = n
a = [0] * n
for i in range(n):
    a[i] = [0] * m
for i in range(m):
    for z in range(m):
        a[i][z] = float(input())

print(a)
