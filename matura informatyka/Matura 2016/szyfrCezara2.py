import string

def cezar(k, t, a):
    wynik = ''
    for i in range(len(t)):
        wynik += a[(a.index(t[i])+int(k)) % 26]
    return wynik


alfabet = list(string.ascii_uppercase)

tekst = input('Do szyfrowania: ')
klucz = int(input('Podaj klucz: '))
jawny = cezar(klucz, tekst.upper(), alfabet)
print(jawny)
