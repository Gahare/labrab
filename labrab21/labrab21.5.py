a = input()
b = ""
dotcount = 0
for i in range(len(a)):
    if a[i] == ".":
        dotcount = dotcount + 1
i = 0
while dotcount != 0:
    if a[i] == "\\":
        b = ''
    elif a[i] == ".":
        b = b + a[i]
        dotcount = dotcount - 1
    else:
        b = b + a[i]
    i = i + 1
print(b[0:len(b) - 1])
