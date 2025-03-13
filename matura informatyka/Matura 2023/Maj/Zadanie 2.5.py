wyniki = []
with open("bin.txt") as f:
    for linia in f:
        dz = 0
        i = 1
        for liczba in linia.strip():
            dz+=(int(liczba)*pow(2,(len(linia.strip())-i)))
            i+=1
        wynik = dz ^ (dz//2)
        wyniki.append(bin(wynik)[2:] + '\n')
        plik = open('wyniki2_5.txt', 'w')
        plik.writelines(wyniki)
        plik.close()
