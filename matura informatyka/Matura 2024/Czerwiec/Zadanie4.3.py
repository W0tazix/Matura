odb = []
n=0
with open('odbiorcy.txt','r') as f:
    for linia in f:
        n+=1
        odb.append(int(linia.rstrip()))
komp = [i+1 for i in range(n)]
k=0
runda1 = [odb[i] for i in range(n)]  
runda2 = [0 for i in range(n)]
licz = 1
while k == 0:
    licz+=1
    for i in range(n):
        runda2[i] = runda1[int(odb[i])-1]
        if runda2[i] == komp[i]:
            k+=1
            print(f'{licz} {runda2[i]}')
            break
    for i in range(n):
        runda1[i]=runda2[i]

        
