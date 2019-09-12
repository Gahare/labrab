a=[]
for i in range(int(input())):
    a.append(int(input()))
for i in range(len(a)):
    b=a[i]
    for z in range(i+1,len(a)):
        if a[i]==a[z]:
            print(i+1)
            print(z+1)