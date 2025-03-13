b=1
c=0
licz=0
n = int(input('podaj n: '))
while n>0:
    a = n%10
    n = n//10
    if (a % 2 == 0):
        c = c + (b * (a//2))
    else:
        c=c+b
        licz+=1
    b=b*10
print(c,licz)