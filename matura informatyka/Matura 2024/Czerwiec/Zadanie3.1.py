licz = 0
sl=0

with open("slowa.txt") as f:
    for slowo in f:
        for litera in slowo:
            if litera.isalpha():
                if licz == 0:
                    if litera == 'k':
                        licz+=1
                elif licz == 1:
                    licz+=1
                elif licz == 2:
                    if litera == "t":
                        print(slowo)
                        sl +=1
                        licz = 0
                    else:
                        licz = 0
        licz=0
print(sl)