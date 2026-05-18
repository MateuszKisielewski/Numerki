def horner(x, wspolczynniki, n):
    wynik = wspolczynniki[0]
    i = 1
    while i < n:
        wynik = wynik * x + wspolczynniki[i]
        i += 1
    return wynik
