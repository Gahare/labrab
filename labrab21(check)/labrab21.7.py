a = input()
b = ""
c = ""
for i in range(1, len(a), 2):
    b = b + a[i]
for i in range(0, len(a), 2):
    c = c + a[i]
for i in range(len(c) - 1, -1, -1):
    b = b + c[i]
print(b)
