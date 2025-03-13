def potega(x,y):
    w=1
    if y == 0:
        return 1
    for i in range(y):
        w=w*x
    return w
n = int(input('Podaj n: '))
u = n
k = 0
m = 0
licz = 0
while n>0:
    k = n%10
    n = n//10
    if k%2!=0:
        m+=(k*potega(10,licz))
        licz+=1
if m == 0:
    print(f'Nieparzysty skrót liczby {u} nie istnieje')
else:
    print(f'Nieparzystym skrótem liczby {u} jest liczba {m}.')