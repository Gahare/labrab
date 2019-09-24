n = int(input())
a = []
mascount = []
masbase = []
for i in range(n):
    a.append(float(input()))
base = a[0]
count = 1
for i in range(1, n):
    if a[i] == base:
        count += 1
    else:
        mascount.append(count)
        masbase.append(base)
        base = a[i]
        count = 1
mascount.append(count)
masbase.append(base)
print(mascount)
print(masbase)
