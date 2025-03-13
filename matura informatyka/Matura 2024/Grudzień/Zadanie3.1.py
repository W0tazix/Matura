from math import sqrt
licz=0
with open("liczby.txt", 'r') as f:
    for liczba in f:
        if sqrt(int(liczba.rstrip())) == int(sqrt(int(liczba.rstrip()))):
            print(liczba)
            licz+=1
print(licz)