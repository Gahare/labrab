a = input()
b = a[0]
firstl = a[0]
check = True
first = False
for i in range(1, len(a)):
    if a[i] == " " and check is True:
        check = False
        first = True
        b = b + a[i]
    if a[i] != " ":
        check = True
        if first is True:
            firstl = a[i]
            b = b + a[i]
            first = False
        else:
            if a[i] == firstl:
                b = b + "."
            else:
                b = b + a[i]
print(b)
