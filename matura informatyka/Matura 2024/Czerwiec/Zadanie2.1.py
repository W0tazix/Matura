
def funkcja(x):
    global wywo
    wywo+=1
    if x == 0:
        return 0
    else:
        return (2 + funkcja(x//2))
    
n = int(input("liczba "))
global wywo
wywo = 0
print(funkcja(n), wywo)
