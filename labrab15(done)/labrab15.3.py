n = int(input())
a = []
suma = 0
for i in range(n):
    a.append(float(input()))
for i in range(n):
    if a[i] % 2 == 1:
        c = a[i]
for i in range(n):
    if a[i] % 2 == 1:
        a[i] = a[i] + c
print(a)
