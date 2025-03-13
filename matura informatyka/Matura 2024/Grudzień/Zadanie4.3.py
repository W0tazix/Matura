def cal(x):
    w=0
    for i in range(len(x)):
        w+=(int(x[i])*pow(10,len(x)-i-1))
    return w

def policz(x,i):
    wynik=0
    lista = sorted(x)[::-1]
    if len(x)>=i:
        for k in range(i):
            wynik+=lista[k]
    else:
        return 0
    return wynik

z=0
maks2=0
maks3=0
maks5=0
with open("prostokaty.txt", 'r') as f:
    for linia in f:
        w=[]
        licz=0
        h=[]
        b=[]
        for numer in linia:
            if numer.isdigit():
                if licz==0:
                    h+=[numer]
                else:
                    b+=[numer]
            else:
                licz=1
        with open("prostokaty.txt", 'r') as f:
            for linia1 in f:
                licz=0
                h2=[]
                b2=[]
                for numer in linia1:
                    if numer.isdigit():
                        if licz==0:
                            h2+=[numer]
                        else:
                            b2+=[numer]
                    else:
                        licz=1
                if h2==h:
                    w+=[cal(b2)]
            if policz(w,2)>maks2:
                maks2=policz(w,2)
            elif policz(w,3)>maks3:
                maks3=policz(w,3)
            elif policz(w,5)>maks5:
                maks5=policz(w,5)
        z+=1
        print(f'zostało {5000-z} linijek')    
            
print(maks2,maks3,maks5)