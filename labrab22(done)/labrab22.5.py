a = open("test5.txt")
b = a.read()
spaces = 0
abz = 0
for i in range(len(b)):
    if b[i] == " ":
        if spaces != 5:
            spaces = spaces + 1
        else:
            abz = abz + 1
    else:
        if spaces == 5:
            abz = abz + 1
        spaces = 0
print(abz)
