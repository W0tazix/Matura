odb = []
n=0
with open('odbiorcy.txt','r') as f:
    for linia in f:
        n+=1
        odb.append(int(linia.rstrip()))
komp = [i+1 for i in range(n)]
i=1
licz=0
for liczba in komp:
    if liczba in odb:
        i+=1
    else:
        licz+=1
        i+=1
print(licz)