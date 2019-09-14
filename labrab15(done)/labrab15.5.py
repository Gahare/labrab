n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
for i in range(n - 1):
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
print(a)
