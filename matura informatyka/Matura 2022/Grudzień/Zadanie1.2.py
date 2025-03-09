dane = []
with open("mecz.txt", 'r') as f:
    for linia in f:
        for litera in linia:
            dane.append(litera)
licza=0
liczb=0
for i in range(len(dane)):
    if dane[i]=="A":
        licza+=1
    elif dane[i]=='B':
        liczb+=1
    if licza>=1000 or liczb>=1000:
        if licza+3<=liczb or liczb+3<=licza:
            print(licza,liczb)
            licza=0
            liczb=0
            break