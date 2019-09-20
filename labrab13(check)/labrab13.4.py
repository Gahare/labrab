import random

a = []
n = int(input())
for i in range(n):
    a.append(random.randint(1, 100))
for i in range(len(a) // 2):
    print(a[i])
    print(a[len(a) - 1 - i])
if len(a) % 2 == 1:
    print(a[len(a) // 2])
