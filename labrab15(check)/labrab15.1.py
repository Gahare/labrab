import random
n = int(input())
a = []
b = []
for i in range(n):
    a.append(random.uniform(-100, 100))
for i in range(n):
    b.append(random.uniform(-100, 100))
for i in range(n):
    a[i], b[i] = b[i], a[i]
print(a)
print(b)
