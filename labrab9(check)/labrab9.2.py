a = input()
b = int(input())
if a == "С":
    a = 1  # sever
elif a == 'З':
    a = 2  # zapad
elif a == 'Ю':
    a = 3  # yug
elif a == 'В':
    a = 4  # vostok
a = a + b
if a == 5:
    a = 1
if a == 0:
    a = 4
if a == 1:
    print('С')
if a == 2:
    print('З')
if a == 3:
    print('Ю')
if a == 4:
    print('В')
