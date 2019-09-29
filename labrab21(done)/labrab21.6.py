a = input()
b = ""
slash = 0
for i in range(len(a)):
    if a[i] == "\\":
        slash = slash + 1
i = 0
if slash == 1:
    print("\\")
else:
    while slash != 0:
        if a[i] == "\\":
            if slash == 1:
                break
            else:
                b = ''
                slash = slash - 1
        else:
            b = b + a[i]
        i = i + 1
print(b[0:len(b) - 1])
