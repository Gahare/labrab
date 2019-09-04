import math
a=[]
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.sort()
if math.sqrt(a[1]**2+a[0]**2)==a[2]:
    print(True)
else:
    print(False)
