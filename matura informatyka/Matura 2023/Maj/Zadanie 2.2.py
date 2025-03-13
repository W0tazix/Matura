c = []
licznik = 0
with open("bin.txt") as f:
    for linia in f:
        c = []
        for liczba in linia.strip():
            c.append(liczba)
        b = 1
        k = 0
        for i in c:
            if k+1 < len(c):
                if c[k] != c[k+1]:
                    b+=1
            k+=1
        if b < 3:
            licznik+=1
plik = open('wyniki2_2.txt' , 'w')
plik.write(f' Liczb składających się z co najwyżej dwóch bloków jest {licznik}')
plik.close()
