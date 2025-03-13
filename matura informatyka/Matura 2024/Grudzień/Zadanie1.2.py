def cnab(c,x):
    b = []
    while c > 0:
        b = b + [c%x]
        c = c//x
    return b

def J(n):
    i = 1
    b = cnab(n,2)
    for liczba in b:
        if liczba == 1:
            print(i)
        i+=1