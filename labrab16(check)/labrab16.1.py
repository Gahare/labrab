n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
nach = a[0]
z = 1
while z < len(a):
    if a[z] == nach:
        del a[z]
    else:
        nach = a[z]
        z = z + 1
print(a)
