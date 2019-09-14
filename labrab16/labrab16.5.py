a = []
n = int(input())
for i in range(n):
    a.append(float(input()))
z = 0
while True:
    try:
        a[z] = a[z]
    except IndexError:
        break
    if a[z] > 0:
        a.insert(z, 0)
        z = z + 1
    z = z + 1
print(a)
