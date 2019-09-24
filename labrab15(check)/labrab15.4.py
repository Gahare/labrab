import random
n = int(input())
a = []
change = False
for i in range(n):
    a.append(random.uniform(-100, 100))
maxvalue = max(a)
minvalue = min(a)
for i in range(n):
    if a[i] == maxvalue or a[i] == minvalue:
        if change is False:
            change = True
            continue
        else:
            change = False
    if change is True:
        a[i] = 0
print(a)
