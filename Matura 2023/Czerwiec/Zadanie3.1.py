dane=[]
with open('anagram.txt','r') as f:
    for linia in f:
        dane.append(linia.rstrip())
        
zrow = 0
pzrow = 0
for linia in dane:
    lz = 0
    lj = 0
    for liczba in linia:
        if liczba == '0':
            lz+=1
        elif liczba == '1':
            lj+=1
    if lj==lz:
        zrow+=1
    elif abs(lj-lz) == 1:
        pzrow+=1
        
print(zrow,pzrow)