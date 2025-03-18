pi = []
with open('pi.txt') as f:
    for linia in f:
        pi.append(linia.rstrip())

maks = 0
pom = 0
pocz = 0
przel = 0
licz = 0
t = []
wynik = []
for i in range(len(pi)-1):
    if licz==0:
        pom=i
    if przel == 1:
            if pi[i]>=pi[i+1]:
                licz+=1
                t.append(pi[i])
            else:
                if licz > maks:
                    t.append(pi[i])
                    maks = licz
                    pocz = pom
                    wynik = t
                licz = 0
                przel = 0
                t = []
    if przel == 0:
        if pi[i]<=pi[i+1]:
            licz+=1
            t.append(pi[i])
        else:
            przel = 1
            licz+=1
            t.append(pi[i])
    
print(pocz,wynik)
