l = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
base = a[0]
basein = 0
count = 1
for i in range(1, n):
    if a[i] == base:
        count += 1
    else:
        if count > l:
            for z in range(count):
                a.remove(a[basein])
            a.insert(0, basein)
        base = a[i - z]
        count = 1
        basein = i - z
print(a)
