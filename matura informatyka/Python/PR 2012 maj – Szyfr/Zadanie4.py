from operator import index
from pickletools import long1

slownik = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def zaszyfr(jawny, klucz,slownik):
    szyfr = []
    k=0
    for i in range(len(jawny)):
        if k>len(klucz)-1:
            k=0
        l1 = ord(jawny[i])
        l2 = slownik.index(klucz[k])+1
        dupa = l1 + l2
        if dupa>90:
            dupa-=26
        szyfr.append(chr(dupa))
        k+=1
    return "".join(szyfr)
print(zaszyfr("LATO","WODA",slownik))
print(zaszyfr("MARTA","TOR",slownik))

def odszyfr(szyfr,klucz,slownik):
    jawny = []
    k = 0
    for i in range(len(szyfr)):
        if k > len(klucz) - 1:
            k = 0
        l1 = ord(szyfr[i])
        l2 = slownik.index(klucz[k]) + 1
        dupa = l1 - l2
        if dupa < 65:
            dupa += 26
        jawny.append(chr(dupa))
        k += 1
    return "".join(jawny)
print(odszyfr("IPXP","WODA",slownik))
print(odszyfr("GPJNP","TOR",slownik))

tj=[]
klucze1 = []
sz = []
klucze2 = []
odp1 = []
odp2 = []


with open("tj.txt","r") as f:
    for line in f:
        tj.append(line.rstrip())

with open("klucze1.txt","r") as f:
    for line in f:
        klucze1.append(line.rstrip())

with open("sz.txt","r") as f:
    for line in f:
        sz.append(line.rstrip())

with open("klucze2.txt","r") as f:
    for line in f:
        klucze2.append(line.rstrip())

for i in range(len(tj)):
    odp1.append(zaszyfr(tj[i],klucze1[i],slownik))

for i in range(len(sz)):
    odp2.append(odszyfr(sz[i],klucze2[i],slownik))

with open("wynik4a.txt","w") as f:
    f.write("\n".join(odp1))

with open("wynik4b.txt","w") as f:
    f.write("\n".join(odp2))