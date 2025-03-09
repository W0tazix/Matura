with open("pi.txt") as f:
    i=0
    c=[]
    wynik=0
    for liczba in f:
        c.append(liczba.strip())
        b = int(liczba.strip())
        i+=1
        if i == 2:
            if (int(c[0])*10 + int(c[1])) > 90:
                wynik+=1
                c = []
                c.append(b)
                i = 1
            else:
                c = []
                c.append(b)
                i = 1
print(wynik)