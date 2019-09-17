a = int(input())
a0 = a // 100
a1 = a // 10 - a0 * 10
a2 = a % 10
if a0 >= a1 >= a2 or a2 >= a1 >= a0:
    print(True)
else:
    print(False)
