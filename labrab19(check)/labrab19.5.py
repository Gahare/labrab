m = int(input())  # vniz
a = [0] * m
allsum = 0
promsum=0
for i in range(m):
    a[i] = [0] * m
for i in range(m):
    for j in range(m):
        a[i][j] = float(input())
for i in range(1, m):
    w = i
    for z in range(m - i):
        promsum=promsum+a[w][z]
        w = w + 1
    allsum= allsum + promsum
    print(promsum)
    promsum=0
for i in range(1, m):
    w = i
    for z in range(m - i):
        promsum=promsum+a[z][w]
        w = w + 1
    allsum= allsum + promsum
    print(promsum)
    promsum=0
print(a)
print(allsum)
