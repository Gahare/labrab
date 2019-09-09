import math


def rings(r1, r2):
    s1 = r1 ** 2 * math.pi
    s2 = r2 ** 2 * math.pi
    return s1 - s2


a = float(input())
b = float(input())
print(rings(a, b))
