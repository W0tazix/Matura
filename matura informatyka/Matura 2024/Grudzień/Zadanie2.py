def F(x,p):
    global licz
    licz += 1
    if x==0:
        return 0
    else:
        c = x%p
        if c%2 == 1:
            return F(x//p,p)+c
        else:
            return F(x//p,p)-c
licz = 0

def sprawdz(p):
    max = 0
    for x in range(100):
        if F(x,p) == 0:
            if x > max:
                max = x
    return max
        