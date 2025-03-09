alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
licz = 0

with open("slowa.txt") as f:
    for slowo in f:
        l1 = [0 for i in range(26)]
        for litera in slowo:
            if litera.isalpha():
                l1[alf.index(litera)] += 1
        if max(l1)>=(len(slowo.rstrip())/2):
            print(slowo,alf[l1.index(max(l1))], max(l1), len(slowo.rstrip()))
            licz+=1