a = open('test.txt', "r")
i = 0
b = a.read()
c = ""
check = False
for i in range(len(b)):
    if check == True:
        c = c + b[i]
    if b[i] == " ":
        check = True
a.close()
a = open("test.txt", "w")
a.write(c)
a.close()
