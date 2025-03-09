dane = []
with open("mecz.txt", 'r') as f:
    for linia in f:
        for litera in linia:
            dane.append(litera)
            
licza=0
liczb=0
passa=0
maxa=0
maxb=0
maks=0
for i in range(len(dane)):
    if dane[i]=="A":
        licza+=1
        if liczb>=10:
            passa+=1
            if liczb>maxb:
                maxb=liczb
        liczb=0
    elif dane[i]=='B':
        liczb+=1
        if licza>=10:
            passa+=1
            if licza>maxa:
                maxa=licza
        licza=0
        
if maxa>maxb:
    maks = maxa
    litera = 'A'
if maxb>maxa:
    maks = maxb
    litera = 'B'
    
print(passa, litera,maks)
        