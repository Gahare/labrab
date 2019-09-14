n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
z = 0
b = {}
count = 0
while True:
    try:
        a[z] = a[z]
    except IndexError:
        break
    if a[z] in b:
        b[a[z]] += 1
    else:
        b[a[z]] = 1
    z = z + 1
z = 0
for i in b:
    if b[i] == 2:
        while True:
            try:
                a[z] = a[z]
            except IndexError:
                break
            if a[z] == i:
                a.remove(a[z])
                count += 1
            else:
                if count < 2:
                    z = z + 1
                else:
                    break
print(a)
