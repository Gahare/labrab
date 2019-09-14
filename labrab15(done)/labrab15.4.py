n = int(input())
a = []
change = False
for i in range(n):
    a.append(float(input()))
mux = max(a)
mix = min(a)
for i in range(n):
    if a[i] == mux or a[i] == mix:
        if change is False:
            change = True
            continue
        else:
            change = False
    if change is True:
        a[i] = 0
print(a)
