def f(t,n,i):
    if (i)==n:
        return 0
    k=0
    for y in range(1,n):
        if y!=i:
            k=k+t[y]
    if t[i]<(k//n):
        t[i]=t[i]*3
    else:
        t[i]=t[i]//3
    f(t,n,i+1)
    
t=[1, 2, 3, 4, 5]
f(t, 5, 1)
