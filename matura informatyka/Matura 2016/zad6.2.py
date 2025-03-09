import string
import sys
sys.set_int_max_str_digits(0)

def cezar(k, t, a):
    wynik = ''
    if len(k.rstrip()) == 0:
        return 'BŁĄD! Brak klucza do odszyfrowania!'
    for i in range(len(t)):
        wynik += a[(a.index(t[i])-int(k.rstrip())) % len(a)]
    return wynik

dane = []
k = ''
wyniki = []
a = list(string.ascii_uppercase)
with open('dane_6_2.txt') as f:
    for linia in f:
        for znak in linia.rstrip():
            if znak in a:
                dane.append(znak)
            else:
                k += (znak.rstrip())
        wyniki.append(f'{cezar(k, dane, a)} \n')
        dane = []
        k = ''
i = 0
with open('wyniki_6_2.txt','w') as f:
        f.writelines(wyniki)
