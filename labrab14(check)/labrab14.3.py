a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
masmin=max(a)
for i in range(len(a)):
    if i%2==1 and a[i]<masmin:
        masmin=a[i]
        z=i+1
print(z)
