# расстояние между точками на оси, произведение
ax = float(input())
bx = float(input())
cx = float(input())
if cx>ax and cx<bx:
    ac = abs(ax - cx)
    bc = abs(bx - cx)
    print(ac * bc)
else:
    print('Некорректные данные')
