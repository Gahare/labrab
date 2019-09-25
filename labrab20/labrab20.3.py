a = input()
check = 0
for i in range(len(a)):
    for z in range(97, 123):
        if ord(a[i]) == z:
            check = check + 1
print(check)
