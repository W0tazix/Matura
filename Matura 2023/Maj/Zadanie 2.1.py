def dznabin(n):
    c = []
    i = 1
    while  n != 0:
        c.append(n%2)
        n=n//2
        i+=1
    return c
    
def ileblokow(c):
    b = 1
    k = 0
    for i in c:
        if k+1 < len(c):
            if c[k] != c[k+1]:
                b+=1
        k+=1
    return b


def ileblokow2(n):
    b = 1
    pop = n%2
    n = n//2
    while  n != 0:
        cyf=n%2
        if cyf != pop:
            b+=1
            pop = cyf
        n=n//2 
    return b

n = int(input("podaj liczbę"))
print(f'liczba bloków wynosi {ileblokow2(n)}')