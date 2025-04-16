licz = 0
liczby1 = []
liczby2 = []
pom = ''

with open('liczby_przyklad.txt.') as f:
    for linia in f:
        for liczba in linia:
            if licz == 0:
                if liczba == '\n':
                    liczby1.append(int(pom))
                    licz+=1
                    pom = ''
                elif liczba == ' ':
                    liczby1.append(int(pom))
                    pom = ''
                else:
                    pom+=liczba
            else:
                if liczba == ' ':
                    liczby2.append(int(pom))
                    pom = ''
                else:
                    pom+=liczba
    liczby2.append(int(pom))

for liczba in liczby2:
    l1 = soted(liczby1.copy())
    for dzielnik in l1
        if liczba%dzielnik==0:
            l1.
