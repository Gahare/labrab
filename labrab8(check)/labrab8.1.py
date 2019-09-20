a = int(input())
b = int(input())
if a != b:
    c = max(a, b)
    a += c
    b += c
else:
    a, b = 0, 0
print(a)
print(b)
