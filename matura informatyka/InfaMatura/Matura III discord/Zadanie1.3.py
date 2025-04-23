def dec_to_bin(n):
    l=0
    wynik = ""
    if n == 0:
        return "0"
    while n > 0:
        reszta = n % 2
        if reszta == 0:
            wynik = "0" + wynik
        else:
            wynik = "1" + wynik
        n = n // 2
        l+=1
    return l

n = int(input("Podaj liczbę graczy: "))
x = int(input("Podaj wykrzyczaną liczbę: "))

print(f'Pije osoba z numerem {dec_to_bin(x)%n}')