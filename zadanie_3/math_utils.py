# math_utils.py

def horner(x, wspolczynniki, n):
    """
    Oblicza wartość wielomianu schematem Hornera.
    wspolczynniki: tablica współczynników od najwyższej potęgi do najniższej.
    """
    wynik = wspolczynniki[0]
    i = 1
    while i < n:
        wynik = wynik * x + wspolczynniki[i]
        i += 1
    return wynik

def wartosc_bezwzgledna(x):
    """Iteracyjna/warunkowa implementacja wartości bezwzględnej."""
    if x < 0:
        return -x
    return x