a = int(input())
d = a
b = int(input())
c = 0
while a > 0:
    a = a - b
    c = c + 1
c = c - 1
print(d - b * c)
