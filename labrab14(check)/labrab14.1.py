import random

a = []
n = int(input())
k = int(input())
l = int(input())
sred = 0
num = 0
for i in range(n):
    a.append(random.randint(1, 100))
for i in range(k, l):
    sred = sred + a[i]
    num = num + 1
print(round(sred / num, 5))
