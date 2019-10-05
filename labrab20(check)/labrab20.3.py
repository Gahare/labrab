a = input()
check = 0
for i in range(len(a)):
    if 122>=ord(a[i])>=97:
        check = check + 1
print(check)
