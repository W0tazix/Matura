pom = ''
licz = 0
liczby1 = []
liczby2 = []
with open('liczby.txt') as f:
    for linia in f:
        for liczba in linia:
            if liczba == '\n':
                if licz == 0:
                    liczby1.append(int(pom))
                else:
                    liczby2.append(int(pom))
                pom = ''
                licz+=1
            else:
                if liczba == ' ':
                    if licz == 0:
                        liczby1.append(int(pom))
                    else:
                        liczby2.append(int(pom))
                    pom = ''
                else:
                    pom+=liczba
            
liczby1 = sorted(liczby1)     
print(liczby1[-100])
            
            
        
