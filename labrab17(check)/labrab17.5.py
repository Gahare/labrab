import math

changefactora = 0
changefactorb = 0
changefactorc = 0
a = []
xmax = 0
ymax = 0
for i in range(int(input()) * 2):
    a.append(float(input()))
ax = a[0]
ay = a[1]
bx = a[2]
by = a[3]
cx = a[4]
cy = a[5]
ab = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
ac = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
bc = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
for i in range(6, len(a), 2):
    lastax = ax
    lastay = ay
    ax = a[i]
    ay = a[i + 1]
    newab = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
    if newab > ab:
        changefactora = changefactora + (newab - ab)
        potentialax = a[i]
        potentialay = a[i + 1]
    newac = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
    if newac > ac:
        changefactora = changefactora + (newac - ac)
        potentialax = a[i]
        potentialay = a[i + 1]
    ax = lastax
    ay = lastay

    lastbx = bx
    lastby = by
    bx = a[i]
    by = a[i + 1]
    newab = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
    if newab > ab:
        changefactorb = changefactorb + (newab - ab)
        potentialbx = a[i]
        potentialby = a[i + 1]
    newbc = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
    if newbc > bc:
        changefactorb = changefactorb + (newbc - bc)
        potentialbx = a[i]
        potentialby = a[i + 1]
    bx = lastbx
    by = lastby

    lastcx = cx
    lastcy = cy
    cx = a[i]
    cy = a[i + 1]
    newbc = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
    if newbc > bc:
        changefactorc = changefactorc + (newbc - bc)
        potentialcx = a[i]
        potentialcy = a[i + 1]
    newac = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
    if newac > ac:
        changefactorc = changefactora + (newac - ac)
        potentialcx = a[i]
        potentialcy = a[i + 1]
    cx = lastcx
    cy = lastcy
    if changefactora > 0 or changefactorb > 0 or changefactorc > 0:
        if max(changefactora, changefactorb, changefactorc) == changefactora:
            ax = a[i]
            ay = a[i + 1]
        elif max(changefactora, changefactorb, changefactorc) == changefactorb:
            bx = a[i]
            by = a[i + 1]
        else:
            cx = a[i]
            cy = a[i + 1]
ab = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
ac = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
bc = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
p = ab + ac + bc
print(p)
print(ax, ay, "\n", bx, by, "\n", cx, cy)
# программа подставляет вместо точек новые координаты, создает 2 фактора, меняет координаты
# и идет дальше
