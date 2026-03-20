def horner(x, wspolczynniki, n):
    if n == 0:
        return 0.0
    wynik = wspolczynniki[0]
    i = 1
    while i < n:
        wynik = wynik * x + wspolczynniki[i]
        i += 1
    return wynik
