a = 0
with open("bin.txt") as f:
    for linia in f:
        b = linia
        if int(b) > int(a):
            a = b
plik = open('wyniki2_3.txt', 'w')
plik.write(a)
plik.close()
