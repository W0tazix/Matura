pi = []
with open('pi.txt') as f:
    for linia in f:
        pi.append(linia.rstrip())

for i in range(len(pi)-6):
    if pi[i]<=pi[i+1] and pi[i+1]<=pi[i+2] and pi[i+2]>=pi[i+3] and pi[i+3]>=pi[i+4] and pi[i+4]>=pi[i+5]:
        print(pi[i],pi[i+1],pi[i+2],pi[i+3],pi[i+4],pi[i+5])