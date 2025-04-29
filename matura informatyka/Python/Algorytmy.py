# Algorytm Euklidesa, czyli od dłuższego patyczka odcinamy krótszy dopóki nie będą równe
# W ten sposób znajdujemy NWD

def nwd1(a,b):
    while(a!=b):
        if a>b:
            a-=b
        else:
            b-=a
    return a


# Można to również zapisać w sposób szybszy używając modulo zamiast kilkukrotnie
# odejmować tą samą liczbe jeśli jedna z nich jest dużo większa

def nwd2(a,b):
    while(a!=0 and b!=0):
        if a>b:
            a%=b
        else:
            b%=a
    if a>b:
        return a
    else:
        return b
    
# Można też w sposób rekurencyjny

def nwd3(a,b):
    if b==0:
        return a
    else:
        return nwd3(b,a%b)


# Wyszukiwanie max/min
# Bardzo prosty algorytm, wystarczy przeiterować po liście i sprawdzić czy element jest mniejszy czy większy
# od pierwszego elementu w liście
# W razie potrzeby zmieniamy nasze minimum/maksimum na kolejną wartość i końcowo otrzymujemy nasz wynik
# Ale najpierw ją zdefiniuje

lista = [3,5,53,2,-34,346,458]

# I teraz szukamy minimum

min = lista[0]
for i in lista:
    if i<min:
        min=i
print(f'minimum wynosi {min}')

# I na takiej samej zasadzie maksimum

max = lista[0]
for i in lista:
    if i>max:
        max=i
print(f'maksimum wynosi {max}')


# Sortowanie przez scalanie
# W tym algorytmie chodzi o to żeby najpierw podzielić to na mniejsze listy a potem tylko po dwie liczby na raz sortować
# Potem jak mamy już dwie posortowane listy to sprawdzamy pomiędzy nimi wartości od początku (bo wiemy że tam są najmniejsze)
# Nie musimy się martwić kolejnymi wartościami bo tam już są większe liczby
# Potem liczbę która jest mniejsza dodajemy do rozwiązania i przesuwamy index tej listy z której wzieliśmy liczbę tak,
# żeby porównywać teraz następną liczbę z tej listy
def merge(left, right): # Tutaj porówujemy ze sobą dwie mniejsze tablice i łączymy w jedną
    result = [] # Definiujemy nasz wynik (na razie pusty)
    i = j = 0 # Definiujemy zerowe indeksy
    while i < len(left) and j < len(right): # Dopóki w którejś liście nie skończą nam się numery
        if left[i] < right[j]: # Sprawdzamy która liczba jest mniejsza
            result.append(left[i]) # Dodajemy mniejszą liczbę do rozwiązania
            i += 1 # Przechodzimy o indeks dalej żeby nie sprawdzać już liczby dodanej do rozwiązania
        else: # Tu to samo tylko gdyby liczba z prawej była mniejsa LUB LICZBY BYŁY RÓWNE
            result.append(right[j])
            j += 1
    result.extend(left[i:]) # Dodajemy ostanią liczbę na koniec listy (musi być extend bo append doda liste a nie int)
    result.extend(right[j:]) # Musimy dodać zobu list i z jednej doda się nic a z drugiej ta jedna co nam została
    return result

def merge_sort(arr): # Tutaj po prostu wywołujemy funkcje i dzielimy na kolejne mniejsze listy
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# Wyznaczanie Miejsc Zerowych Metodą Połowienia
def f(x):
    return x**2-60
def miejsce_zerowe(a, b, epsilon): # a i b to skrajne miejsca naszego zakresu poszukiwań miejsca zerowego funkcji
    if f(a) * f(b) > 0:
        return None  # Funkcja nie zmienia znaku – metoda nie zadziała
    while abs(b - a) > epsilon: # Sprawdzamy czy różnica jest większa od błędu
        c = (a + b) / 2 # Dzielimy na pół zakres poszukiwań
        if f(c) == 0: 
            return c
        elif f(a) * f(c) < 0: # Sprawdzamy z której strony mamy obciąć nasz zakres na pół
            b = c
        else:
            a = c
    return (a + b) / 2

# Wyznaczanie pierwiastka kwadratowego z liczby całkowitej metodą połowienia
def pierwiastek(x,eps):
    a=0 # Początek zakresu w którym szukamy odpowiedzi
    b=x # Końcem zakresu będzie x ponieważ żadna liczba całkowita nie będzie mniejsza niż jej kwadrat
    while abs(b-a)>eps:
        c = (a+b)/2
        if x<c*c:
            b=c
        else:
            a=c
    return c

# Potęgowanie iteracyjne
# To chyba proste, sprawdzamy dwie opcje albo jest potega 0 albo 1
# Jeśli nie to mnożymy przez siebie tyle razy ile trzeba
def potiter(a,n):
    wynik=a
    if n == 0:
        return 1
    elif n == 1:
        return a
    for i in range(n-1):
        wynik*=a
    return wynik

# Potęgowanie rekurencyjne
def potreku(a,n):
    if n == 0:
        return 1
    return potreku(a,n-1)*a # Wywołuje mniejszą potęgę którą później podniesie do potęgi większej
# Program robi to do tego momentu w którym nie osiągnie jeden które potem będzie mnożył za każdym zakończeniem wywołania