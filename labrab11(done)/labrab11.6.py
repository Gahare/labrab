a = 1
b = 0
n = int(input())
k = 2
while True:
    k = k + 1
    if k % 2 == 1:
        b = b + a
    else:
        a = a + b
    if b == n or a == n:
        break
print(k)
