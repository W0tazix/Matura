def cal(x):
    w=0
    for i in range(len(x)):
        w+=(int(x[i])*pow(10,len(x)-i-1))
    return w

maks = 0
mini = 999999999
with open("prostokaty.txt", 'r') as f:
    for linia in f:
        i=0
        licz=0
        a=[]
        b=[]
        for numer in linia:
            if numer.isdigit():
                if licz==0:
                    a+=[numer]
                else:
                    b+=[numer]
            else:
                i=0
                licz=1
        pole = cal(a)*cal(b)
        if pole>maks:
            maks = pole
        elif pole<mini:
            mini = pole
print(maks,mini)