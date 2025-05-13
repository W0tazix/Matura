dane = []
with open("dane.txt") as f:
    for line in f:
        dane.append(line.rstrip())

# Podpunkt a
licznik = 0
for linia in dane:
    if linia[0] == linia[-1]:
        licznik+=1
print(f'Podpunkt a: {licznik}')

#Podpunkt b
licznik = 0
for linia in dane:
    linia = int(linia,8)
    linia = str(linia)
    if linia[0] == linia[-1]:
        licznik += 1

print(f'Podpunkt b: {licznik}')

#Podpunkt c
k = 0
odp = []
for linia in dane:
    for i in range(len(linia)-1):
        if linia[i]<=linia[i+1]:
            k += 1
    if k == len(linia)-1:
        odp.append(int(linia))
    k=0

print(f'Podpunkt c: {len(odp)}\n'
      f'Najmniejsza liczba {min(odp)}\n'
      f'Największa liczba {max(odp)}')
