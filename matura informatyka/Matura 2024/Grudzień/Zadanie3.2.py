def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def dzielniki(x):
    dz = []
    for i in range(2,x+1):
        if x % i == 0:
            dz += [i]
    return dz
dziel = []
wynik = []
with open("liczby.txt", 'r') as f:
    for liczba in f:
        dziel = dzielniki(int(liczba))
        wynik=[]
        for l in dziel:
            if czy_pierwsza(l):
                wynik+=[l]
        if len(wynik)>=5:
            print(liczba.rstrip())
        