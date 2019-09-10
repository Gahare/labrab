n = int(input())
a = int(input())
b = int(input())
z = []
z.append(a)
z.append(b)
for i in range(2, n + 1):
    z.append(z[i - 2] + z[i - 1])
print(z)
