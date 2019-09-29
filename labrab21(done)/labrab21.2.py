a = input()
minwordlen = len(a)
wordlen = 0
check = True
for i in range(len(a)):
    if a[i] == " " and check is True:
        check = False
        if wordlen < minwordlen:
            minwordlen = wordlen
            wordlen = 0
    if a[i] != " ":
        check = True
        wordlen = wordlen + 1
if wordlen < minwordlen:
    minwordlen = wordlen
print(minwordlen)
