n = int(input())
a = []
b = []
for i in range(n):
    a.append(float(input()))
for i in range(n):
    b.append(float(input()))
for i in range(n):
    a[i], b[i] = b[i], a[i]
print(a)
print(b)
