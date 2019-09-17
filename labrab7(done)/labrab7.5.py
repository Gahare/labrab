a = int(input())
a0 = a // 1000
a1 = a // 100 - a0 * 10
a2 = a // 10 - a0 * 100 - a1 * 10
a3 = a % 10
if a == a3 * 1000 + a2 * 100 + a1 * 10 + a0:
    print(True)
else:
    print(False)
