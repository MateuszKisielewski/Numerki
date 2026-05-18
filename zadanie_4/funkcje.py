import math

def schemat_hornera(argument, wspolczynniki, dlugosc):
    wynik = wspolczynniki[0]
    indeks = 1
    while indeks < dlugosc:
        wynik = wynik * argument + wspolczynniki[indeks]
        indeks += 1
    return wynik

def funkcja_wielomianowa(argument):
    wspolczynniki = [2.0, -3.0, 1.0, 5.0]
    return schemat_hornera(argument, wspolczynniki, 4)

def funkcja_trygonometryczna(argument):
    return math.cos(argument) + 2.0

def funkcja_wykladnicza(argument):
    return math.exp(argument)