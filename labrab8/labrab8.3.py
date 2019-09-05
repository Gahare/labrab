import math
ax=float(input())
ay=float(input())
bx=float(input())
by=float(input())
cx=float(input())
cy=float(input())
dab=math.sqrt((bx-ax)**2+(by-ay)**2)
dac=math.sqrt((cx-ax)**2+(cy-ay)**2)
if dab>dac:
    print('c')
    print(dac)
else:
    print('b')
    print(dab)
