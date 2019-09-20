n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
nach = a[0]
z = 1
while True:
    try:
        a[z] = a[z]
    except IndexError:
        break
    if a[z] == nach:
        del a[z]
    else:
        nach = a[z]
        z = z + 1
print(a)
