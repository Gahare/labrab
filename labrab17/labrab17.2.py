l = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
base = a[0]
basein = 0
count = 1
w = 1
while True:
    try:
        a[w] = a[w]
    except IndexError:
        if count > l:
            for z in range(count):
                del a[basein]
            a.insert(basein, 0)
        break
    if a[w] == base:
        count += 1
    else:
        if count > l:
            for z in range(count):
                del a[basein]
            a.insert(basein, 0)
            base = a[w - z]
            count = 1
            basein = w - z
            w = w - z
        base = a[w]
        basein = w
    w = w + 1
print(a)
