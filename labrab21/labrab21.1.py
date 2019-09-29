a = input()
check = True
word = 0
for i in range(len(a)):
    if a[i] == " " and check is True:
        word = word + 1
        check = False
    if a[i] != " ":
        check = True
if check is True:
    word = word + 1
print(word)
