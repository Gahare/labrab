name = input()
n = int(input())
k = int(input())
name = name + ".txt"
a = open(name, "w")
for i in range(n):
    for j in range(k):
        a.write("*")
    a.write("\n")
a.close()
