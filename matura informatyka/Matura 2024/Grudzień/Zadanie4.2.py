def cal(x):
    w=0
    for i in range(len(x)):
        w+=(int(x[i])*pow(10,len(x)-i-1))
    return w
am=0
bm=0
maks = 0
i=0
a=[]
b=[]
a2=[]
b2=[]
with open("prostokaty.txt", 'r') as f:
    for linia in f:
        licz=0
        if i == 0:
            for numer in linia:
                if numer.isdigit():
                    if licz==0:
                        a+=[numer]
                    else:
                        b+=[numer]
                else:
                    licz=1
            i+=1
        else:
            for numer in linia:
                if numer.isdigit():
                    if licz==0:
                        a2+=[numer]
                    else:
                        b2+=[numer]
                else:
                    licz=1
            if cal(a2)<=cal(a):
                if cal(b2)<=cal(b):
                    i+=1
                    if i>maks:
                        maks=i
                        am=cal(a2)
                        bm=cal(b2)
                else:
                    i=1
            else:
                i=1
            a=a2
            b=b2
            a2=[]
            b2=[]

print(maks,am,bm)