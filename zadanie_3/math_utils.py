# math_utils.py

def horner(x, wspolczynniki, n):
 wynik = wspolczynniki[0]
    i = 1
    while i < n:
        wynik = wynik * x + wspolczynniki[i]
        i += 1
    return wynik

def wartosc_bezwzgledna(x):
    if x < 0:
        return -x
    return x