import random
a=[]
n=int(input())
for i in range(n):
   a.append(random.randint(1,100))
for i in range(len(a)):
    if i%2==0:
        print(a[i])
for i in range(len(a),0,-1):
    if i%2==1:
        print(a[i])