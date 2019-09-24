import random
n = int(input())
a = []
for i in range(n):
    a.append(random.uniform(-100, 100))
for i in range(n - 1):
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
print(a)
