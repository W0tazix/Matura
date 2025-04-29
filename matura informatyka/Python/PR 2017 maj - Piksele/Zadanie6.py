def polacz(lista):
    odp=0
    i=1
    for znak in lista:
        odp+=znak*10**(len(lista)-1)/i
        i*=10
    return int(odp)
linie = []
with open('przyklad.txt') as f:
    for linia in f:
        linie.append(linia)

liczba=[]
dane = []
dane2 = []
l=[]
for linia in linie:
    for znak in linia:
        if znak.isdigit():
            liczba.append(int(znak))
        else:
            l.append(polacz(liczba))
            dane2.append(polacz(liczba))
            liczba = []
    dane.append(l)
    l=[]
print(f'Zadanie 6.1 maksymalna wartość: {max(dane2)} minimalna wartość: {min(dane2)}')


licznik=0
for wiersz in dane:
    if wiersz != wiersz[::-1]:
        licznik+=1      
print(f'Zadanie 6.2 najmniejsza liczba wierszy, które należy usunąć wynosi: {licznik}')


licznik=0
for j in range(200):
    for i in range(320):
        if j+1<200 and abs(dane[j][i]-dane[j+1][i])>128:
            licznik+=1
        elif j-1>=0 and abs(dane[j][i]-dane[j-1][i])>128:
            licznik+=1
        elif i+1<320 and abs(dane[j][i]-dane[j][i+1])>128:
            licznik+=1
        elif i-1>=0 and abs(dane[j][i]-dane[j][i-1])>128:
            licznik+=1
print(f'Zadanie 6.3 Liczba kontrastujacych sąsiednich pikseli wynosi: {licznik}')


licznik=1
max=0
for i in range(320):
    for j in range(199):
        if dane[j][i] == dane[j+1][i]:
            licznik+=1
        else:
            if licznik>max:
                max=licznik
            licznik=1
    if licznik>max:
        max=licznik
    licznik=1
    
print(f'Zadanie 6.4 długość najdłuższej linii pionowej wynosi: {max}')
