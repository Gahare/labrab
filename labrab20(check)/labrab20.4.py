oth = input()
a = input()
w = 0
end = ''
while w < len(a):
    if a[w] == oth:
        end = end + oth
    end = end + a[w]
    w = w + 1
print(end)
