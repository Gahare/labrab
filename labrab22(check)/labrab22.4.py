a = open("test4.txt")
b = a.read()
c = ''
check = False
for i in range(len(b)):
    if b[i] == " ":
        if check is False:
            c = c + b[i]
            check = True
    else:
        c = c + b[i]
        check = False
a = open('test4.txt', "w")
a.write(c)
a.close()
