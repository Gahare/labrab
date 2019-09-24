n = int(input())
adf = True
x = 0
y = 0
m = n
a = [0] * n
f = n - 1  # shagov do konca setki
napr = 1
fcounter = 0
for i in range(n):
    a[i] = [0] * m
for i in range(m):
    for z in range(m):
        a[i][z] = float(input())
if n == 2:
    print(a[0][0])
    print(a[0][1])
    print(a[1][0])
    print(a[1][1])
else:
    for i in range(n ** 2 - (n - 1 ** 2)):  # chislo povorotov
        for z in range(f):  # inversia x and y
            if napr == 1:
                print(a[x][y])
                x = x + 1
            if napr == 2:
                print(a[x][y])
                y = y + 1
            if napr == 3:
                print(a[x][y])
                x = x - 1
            if napr == 4:
                print(a[x][y])
                y = y - 1
        napr = napr + 1
        if napr == 5:
            napr = 1
        fcounter = fcounter + 1
        if i <= 3:
            if fcounter == 3:
                f = f - 1
                fcounter = 0
        else:
            if fcounter == 2:
                f = f - 1
                fcounter = 0
        if f == 0 and adf is True and fcounter != 0:
            f = 1
            adf = False
