k = int(input('k='))
a = []
n = int(input('n='))
for i in range(n):
    a.append(float(input()))
w = 1
serie = 1
seriebegin = 0
serieend = 0
kseriebegin = 0
kserieend = 0
lastseriebegin = 0
lastserieend = 0
base = a[0]
while True:
    try:
        a[w] = a[w]
    except IndexError:
        lastseriebegin = seriebegin
        lastserieend = serieend
        break
    if a[w] == base:
        serieend = w
    else:
        if serie == k:
            kseriebegin = seriebegin
            kserieend = serieend
        base = a[w]
        serie += 1
        seriebegin = w
        serieend = w
    w = w + 1
knum = a[kseriebegin]
lastnum = a[lastseriebegin]
deltak = kserieend - kseriebegin + 1
deltalast = lastserieend - lastseriebegin + 1
while deltak != 0:
    a.remove(a[kseriebegin])
    deltak -= 1
deltak = kserieend - kseriebegin + 1
while deltalast != 0:
    a.remove(a[lastseriebegin - deltak])
    deltalast -= 1
deltalast = lastserieend - lastseriebegin + 1
while deltak != 0:
    a.insert(kseriebegin, lastnum)
    deltak -= 1
while deltalast != 0:
    a.insert(lastseriebegin, knum)
    deltalast -= 1
print(a)