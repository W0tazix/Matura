def nalis(x):
    w = []
    for i in range(4):
        w += [x%10]
        x = x//10
    return w

def cal(x):
    w=0
    for i in range(4):
        w+=(x[3-i]*pow(10,i))
    return w
wie=0
mni=0
row=0
with open("liczby.txt",'r') as f:
    for liczba in f:
        najm = cal(sorted(nalis(int(liczba.rstrip()))))
        najw = cal(sorted(nalis(int(liczba.rstrip())))[::-1])
        if najw-najm>int(liczba):
            wie+=1
        elif najw-najm<int(liczba):
            mni+=1
        elif najw-najm==int(liczba):
            row+=1
            print(int(liczba))
print(f'większa:{wie} mniejsza:{mni} równa:{row}')