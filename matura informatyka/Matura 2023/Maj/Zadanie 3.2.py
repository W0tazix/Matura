with open("pi.txt") as f:
    i=0
    c=[]
    d=[]
    wynik=0
    for liczba in f:
        c.append(liczba.strip())
        b = int(liczba.strip())
        i+=1
        if i == 2:
            d.append(str(int(c[0])*10 + int(c[1])))
            c = []
            c.append(b)
            i = 1
k = 0
i = 0
c = []
e = []
while i < 100:
    c.append(i)
    i+=1
while k< len(c):
    wynik=0
    l=0
    while l< len(d):
        if int(c[k]) == int(d[l]):
            wynik+=1
        l+=1
    e.append(int(wynik))
    k+=1
i=0
k=e[0]
l=0
wynik=[]
for liczba in e:
    if e[i]<k:
        k=e[i]
        l=i
    i+=1
wynik.append(f'{c[l]} {k}' + '\n')
i=0
k=e[0]
l=0
for liczba in e:
    if e[i]>k:
        k=e[i]
        l=i
    i+=1
wynik.append(f'{c[l]} {k}')
plik = open('wyniki3_2.txt','w')
plik.writelines(wynik)
plik.close()