m = int(input())  # vniz
n = int(input())  # vpravo
a = [0] * n
stolbchet = True
check = False
for i in range(n):
    a[i] = [0] * m
for i in range(n):
    for j in range(m):
        a[i][j] = float(input())
print(a)
for i in range(m):
    for j in range(n):
        if a[j][i] % 2 != 1:
            stolbchet = False
    if stolbchet is True:
        if check is False:
            print(i + 1)
            check = True
    stolbchet = True
if check is False:
    print(0)
