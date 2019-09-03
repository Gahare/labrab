import math
x1 = int(input())
y1 = int(input()) #a
x2 = int(input())
y2 = int(input()) #b
x3 = int(input())
y3 = int(input()) #c
ab = round(math.sqrt((x2-x1)**2+(y2-y1)**2),5)
ac = round(math.sqrt((x3-x1)**2+(y3-y1)**2),5)
bc = round(math.sqrt((x3-x2)**2+(y2-y1)**2),5)
p = ab+ac+bc
s = abs(((x1-x3)*(y2-y3)-(y1-y3)*(x2-x3))/2)
print(p)
print(s)
