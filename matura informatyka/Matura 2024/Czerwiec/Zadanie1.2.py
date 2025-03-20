def binarna(n):
    global liczb
    b = []
    liczb = 0
    while n>0:
        b += [(n%2)]
        n=n//2
        liczb += 1
    return b[::-1]

w = int(input("podaj ilość wierszy"))
k = int(input("podaj ilość kolumn"))
n = int(input("podaj liczbe"))
lista = [[0 for i in range(k)] for i in range(w)]
licz = 0
b = binarna(n)


for wier in range(w):
    for kol in range(k):
        if licz>(liczb-1):
            licz=0
            lista[wier][kol] = b[licz]
            licz+=1
        else:
            lista[wier][kol] = b[licz]
            licz+=1
print(lista[w-1][k-1])