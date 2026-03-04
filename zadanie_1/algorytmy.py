from horner import horner
from kryterium_B import kryterium_B

def f_wielomian(x):
    return horner(x, [1, 0, -1, -2], 4)

def bisekcja(f, a, b, kryterium, wartosc):
    if  f(a) * f(b) >= 0:
        return "iloczyn funkcji większy bądź równy 0"
    else:
        xi = (a + b) / 2
        iteracje = 0

        if kryterium == "a":
            while not kryterium_B(f, xi, wartosc):
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
                xi = (a + b) / 2
                iteracje += 1

        else:
            while iteracje < wartosc:
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
                xi = (a + b) / 2
                iteracje += 1
    return xi, iteracje