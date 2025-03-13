def potega(x,y):
    w=1
    if y == 0:
        return 1
    for i in range(y):
        w=w*x
    return w
def nieparz(n):
    u = n
    k = 0
    m = 0
    licz = 0
    while n>0:
        k = n%10
        n = n//10
        if k%2!=0:
            m+=(k*potega(10,licz))
            licz+=1
    return m

licznik=0
wynik = []
with open('skrot.txt') as f:
    for linia in f:
        if nieparz(int(linia.rstrip())) == 0:
            wynik.append(int(linia.rstrip()))
            licznik+=1
wynik = sorted(wynik)
print(wynik[-1],licznik)
