def quarter(x,y):
    if x > 0:
        if y > 0:
            return(1)
        else:
            return(4)
    if x < 0:
        if y > 0:
            return(2)
        else:
            return(3)

a=float(input())
b=float(input())
print(quarter(a,b))