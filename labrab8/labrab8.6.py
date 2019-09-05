a=float(input())
if a%2==0:
    print('Четное',end=' ')
else:
    print('Нечетное',end=' ')
if a//100!=0:
    print('трехзначное число',end=' ')
else:
    if a//10!=0:
        print('двузначное число',end=' ')
    else:
        print('однозначное число',end=' ')
