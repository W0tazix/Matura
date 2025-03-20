pi = []
with open('pi.txt') as f:
    for linia in f:
        pi.append(linia.rstrip())
licz=0
for i in range(len(pi)-6):
    if pi[i]<=pi[i+1]:
        if pi[i+1]<=pi[i+2]:
            if pi[i+2]>=pi[i+3]:
                if pi[i+3]>=pi[i+4]:
                    if pi[i+4]>=pi[i+5]:
                        print(pi[i],pi[i+1],pi[i+2],pi[i+3],pi[i+4],pi[i+5])
                        licz+=1
print(licz)
