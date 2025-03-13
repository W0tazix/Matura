licz = 0
dl = ''
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
with open("slowa.txt") as f:
    for slowo in f:
        tyl = ''
        for litera in slowo:
            if litera.isalpha():
                tyl += (rot[alf.index(litera)])
        if str(tyl[::-1]) == str(slowo.rstrip()):
            print(slowo)
            if len(slowo.rstrip())>len(dl):
                dl = slowo.rstrip()
            licz +=1
print(licz)
print(dl)