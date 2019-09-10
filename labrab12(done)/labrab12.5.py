def fact2(n):
    a = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            a = a * i
    else:
        for i in range(1, n + 1, 2):
            a = a * i
    return (a)


a = int(input())
print(fact2(a))
