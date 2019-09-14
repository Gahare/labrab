n = int(input())
a = []
b = []
c = []
for i in range(n):
    a.append(float(input()))
base = a[0]
count = 1
for i in range(1, n):
    if a[i] == base:
        count += 1
    else:
        b.append(count)
        c.append(base)
        base = a[i]
        count = 1
b.append(count)
c.append(base)
print(b)
print(c)
