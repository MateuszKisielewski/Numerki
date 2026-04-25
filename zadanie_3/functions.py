# functions.py
import math
import math_utils

def funkcja_liniowa(x):
    # f(x) = 2x - 3
    return 2.0 * x - 3.0

def funkcja_modul(x):
    # f(x) = |x|
    return math_utils.wartosc_bezwzgledna(x)

def funkcja_wielomian(x):
    # f(x) = 2x^3 - 4x^2 + x - 5
    # Współczynniki dla schematu Hornera (od najwyższej potęgi)
    wsp = [2.0, -4.0, 1.0, -5.0]
    return math_utils.horner(x, wsp, len(wsp))

def funkcja_trygonometryczna(x):
    # f(x) = sin(x)
    return math.sin(x)

def funkcja_zlozenie(x):
    # f(x) = sin(|x|)
    return math.sin(math_utils.wartosc_bezwzgledna(x))

def ewaluuj_funkcje(id_funkcji, x):
    """Zwraca wartość wybranej funkcji dla danego x bez użycia instrukcji break/continue."""
    wynik = 0.0
    if id_funkcji == 1:
        wynik = funkcja_liniowa(x)
    elif id_funkcji == 2:
        wynik = funkcja_modul(x)
    elif id_funkcji == 3:
        wynik = funkcja_wielomian(x)
    elif id_funkcji == 4:
        wynik = funkcja_trygonometryczna(x)
    elif id_funkcji == 5:
        wynik = funkcja_zlozenie(x)
    return wynik