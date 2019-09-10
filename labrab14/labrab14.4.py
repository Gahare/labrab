a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
for i in range(1,len(a)-1):
    if i==0:
        if a[i]>a[i]+1:
            z = i
    elif i==len(a):
        if a[i]>a[i]-1:
            z = i
    elif a[i]>a[i-1] and a[i]>a[i+1]:
        z=i
print(z)