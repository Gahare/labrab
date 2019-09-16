a = float(input("Введите год:"))
sto = a // 100
osto = a % 100
if osto > 0:
    sto += 1
print(int(sto), "столетие")
