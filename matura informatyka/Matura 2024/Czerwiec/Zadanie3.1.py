licz = 0
sl=0


# Błąd polega na tym, że wyraz 'ewqcvaapmtvesejgdakkkt' jest sprawdzany na bieżąco i przechodząc
# po kolejnych literach omijamy fragment szukany bo jak znajdziemy k to potem iterujemy po słowie
# omijając potencjalne kolejne rozwiązania bo idziemy jakby dalej
'''
with open("slowa_przyklad.txt") as f:
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
'''

slowa = []

with open("slowa.txt") as f:
    for slowo in f:
        slowa.append(slowo.rstrip())


for slowo in slowa:
    for i in range(len(slowo)-2):
        if slowo[i] == 'k' and slowo[i+2] == 't':
            sl+=1
            print(slowo)
print(sl)

