n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
z = 0
b = {}
count = 0
while z < len(a):
    if a[z] in b:
        b[a[z]] += 1
    else:
        b[a[z]] = 1
    z = z + 1
z = 0
for i in b:
    z = 0
    if b[i] == 2:
        while z < len(a):
            if a[z] == i:
                del a[z]
                count += 1
            else:
                if count < 2:
                    z = z + 1
                else:
                    count = 0
                    break
print(len(a))
print(a)
