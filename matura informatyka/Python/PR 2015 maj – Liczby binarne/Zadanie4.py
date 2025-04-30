
dane = []
with open('liczby.txt') as f:
    for linia in f:
        dane.append(linia.rstrip())


    
# Zadanie 4.1
licznik=0
for linia in dane:
    jedynki = 0
    zera = 0
    for znak in linia:
        if znak == "1":
            jedynki+=1
        else:
            zera+=1
    if zera>jedynki:
        licznik+=1
print(f'Zadanie 4.1 {licznik}')
            
          
# Zadanie 4.2
przezdwa = 0
przezosiem = 0
for linia in dane:
    if linia[-1]=='0':
        przezdwa+=1
    if linia[-3:]=='000':
        przezosiem+=1
print(f'Zadanie 4.2 liczb podzielnych przez dwa jest {przezdwa}, a przez osiem {przezosiem}')


# Zadanie 4.3
max1 = min1 =int(dane[0],2)
max2 = min2 = dane[0]
for linia in dane:  
    if int(linia,2)>max1:
        max1 = int(linia,2)
        max2 = linia
    if int(linia,2)<min1:
        min1 = int(linia,2)
        min2 = linia
print(f'Zadanie 4.3 maksimum znajduje sie w linii: {dane.index(max2)+1} a minumim: {dane.index(min2)+1}')
