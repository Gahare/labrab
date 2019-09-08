a = float(input())
a = -a
n = int(input())
l = 1
for i in range(1, n + 1):
    l = l + a ** i
print(l)
