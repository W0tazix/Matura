import itertools

def anagramy(slowo):
    t = itertools.permutations(list(slowo))
    permutacje = [''.join(p) for p in t]
    p_bez_powtorzen = [i for i in permutacje if i[0]=='1']
    print(set(p_bez_powtorzen))
     
dane=[]
with open('anagram.txt','r') as f:
    for linia in f:
        dane.append(linia.rstrip())
        