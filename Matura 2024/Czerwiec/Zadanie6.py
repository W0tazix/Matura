def cnab(n, x):
    b=[]
    while n>0:
        b = b + [n%x]
        n = n//x
    return b[::-1]