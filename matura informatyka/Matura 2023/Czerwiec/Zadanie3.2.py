import itertools

def anagramy(slowo):
    t = itertools.permutations(list(slowo))
    permutacje = [''.join(p) for p in t]
    p_bez_powtorzen = [i for i in permutacje if i[0]=='1']
    return set(p_bez_powtorzen)
     
dane=[]
with open('przyklad.txt','r') as f:
    for linia in f:
        if len(linia.rstrip())==8:
            dane.append(linia.rstrip())

maks = 0
pom = []
for liczba in dane:
    if maks < len(anagramy(liczba)):
        maks = len(anagramy(liczba))
        pom.append(liczba)

wynik = []

for liczba in pom:
    if maks == len(anagramy(liczba)):
        wynik.append(liczba)
print(wynik)