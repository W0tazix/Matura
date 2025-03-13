import string
wynik = ''
k = 107
a = list(string.ascii_uppercase)
with open('dane_6_1.txt') as f:
    for linia in f:
        for i in range(len(linia.rstrip())):
            wynik += a[(a.index(linia.rstrip()[i])+k) % 26]
        print(wynik)
        wynik = ''
        