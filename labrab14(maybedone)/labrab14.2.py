a = []
n = int(input())
z = True
for i in range(n):
    a.append(float(input()))
d = a[1] - a[0]
for i in range(2, len(a)):
    if a[i] - a[i - 1] != d:
        z = False
if not z:
    print(0)
else:
    print(d)
