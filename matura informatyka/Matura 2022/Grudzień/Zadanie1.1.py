dane = []
with open("mecz.txt", 'r') as f:
    for linia in f:
        for litera in linia.rstrip():
            dane.append(litera)
            
            
licz=0
for i in range(len(dane)-1):
    if dane[i] != dane[i+1]:
        licz+=1
print(licz)