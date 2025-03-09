import string
import sys
sys.set_int_max_str_digits(0)

def cezar(s1, s2, a):
    k = abs(a.index(s1[0]) - a.index(s2[0]))
    k1 = abs(26 - k)
    for i in range(len(s1)):
        if k != abs(a.index(s1[i]) - a.index(s2[i])):
            if k1 != abs(a.index(s1[i]) - a.index(s2[i])):
                return s1
    return ' '
wynik=''
wyniki=[]
dane=''
dane2=''
a = list(string.ascii_uppercase)
i = 0
with open('dane_6_3.txt') as f:
    for linia in f:
        for znak in linia.rstrip():
            if i == 0:
                if znak in a:
                    dane += znak
                else:
                    i += 1
            else:
                dane2 += znak
        wynik = cezar(dane, dane2, a)
        if wynik != ' ':
            wyniki.append(f'{wynik} \n')
        dane = ''
        dane2 = ''
        i = 0
with open('wyniki_6_3.txt','w') as f:
    f.writelines(wyniki)
