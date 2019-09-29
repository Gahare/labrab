a = input()
count = 0
glas = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
for i in range(len(a)):
    word = a[i].lower()
    if word in glas:
        count = count + 1
print(count)
