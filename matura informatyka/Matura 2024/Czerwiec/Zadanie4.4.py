odb = []
n=0
with open('odbiorcy.txt','r') as f:
    for linia in f:
        n+=1
        odb.append(int(linia.rstrip()))
komp = [i+1 for i in range(n)]
runda1 = [odb[i] for i in range(n)]  
runda2 = [0 for i in range(n)]
licz = 1
k = 0
odp = [0 for i in range(n)]
for i in range(n):
        odp[komp.index(odb[i])] +=1
for i in range(n):
        if odb[i] == komp[odp.index(max(odp))]:
            k+=1

licz=1
for i in range(1):
    l=0
    licz+=1
    odp = [0 for i in range(n)]
    for i in range(n):
        runda2[i] = runda1[int(odb[i])-1]
    for i in range(n):
        odp[komp.index(runda2[i])] +=1
    for i in range(n):
        runda1[i]=runda2[i]
    for i in range(n):
        if runda2[i] == komp[odp.index(max(odp))]:
            l+=1

licz=1
for i in range(3):
    m=0
    licz+=1
    odp = [0 for i in range(n)]
    for i in range(n):
        runda2[i] = runda1[int(odb[i])-1]
    for i in range(n):
        odp[komp.index(runda2[i])] +=1
    for i in range(n):
        runda1[i]=runda2[i]
    for i in range(n):
        if runda2[i] == komp[odp.index(max(odp))]:
            m+=1

licz=1  
while licz<8:
    p=0
    licz+=1
    odp = [0 for i in range(n)]
    for i in range(n):
        runda2[i] = runda1[int(odb[i])-1]
    for i in range(n):
        odp[komp.index(runda2[i])] +=1
    for i in range(n):
        runda1[i]=runda2[i]
    for i in range(n):
        if runda2[i] == komp[odp.index(max(odp))]:
            p+=1
print(f'{k} {l} {m} {p}')    