a = []
n = int(input())
for i in range(n):
    a.append(float(input()))
c = max(a)
d = min(a)
for i in range(n):
    if a[i] == d:
        a.insert(i, 0)
        break
for i in range(len(a)):
    if a[i] == c:
        a.insert(i + 1, 0)
        break
print(a)
