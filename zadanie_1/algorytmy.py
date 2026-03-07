from numpy import cos, exp, sin

from horner import horner

def f_wielomian(x):
    return horner(x, [1, 2, -1, -2], 4)

def df_wielomian(x):
    return horner(x, [3, 4, -1], 3)

def f_trygonometryczna(x):
    return (cos(x) - 0.5)

def df_trygonometryczna(x):
    return -sin(x)

def f_wykladnicza(x):
    return (exp(x) - 7)

def df_wykladnicza(x):
    return exp(x)

def f_zlozenia(x):
    horner_f_zlozenia = horner(x, [1, 0, 0, 7], 4)
    return (horner_f_zlozenia - cos(x) - exp(x))

def df_zlozenia(x):
    horner_df_zlozenia = horner(x, [3, 0, 0], 3)
    return (horner_df_zlozenia + sin(x) - exp(x))

def bisekcja(f, a, b, kryterium, epsilon):
    if  f(a) * f(b) >= 0:
        return "iloczyn funkcji większy bądź równy 0 - brak spełnienia warunków zadania", "Błąd!"
    else:
        xi = (a + b) / 2
        iteracje = 0

        if kryterium == "1":
            while not (abs(f(xi)) < epsilon) and f(xi) != 0:
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
                xi = (a + b) / 2
                iteracje += 1

        else:
            while iteracje < epsilon and f(xi) != 0:
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
                xi = (a + b) / 2
                iteracje += 1
    return xi, iteracje

def styczna(f, df, a, b, kryterium, epsilon):
    if f(a) * f(b) >= 0:
        return "iloczyn funkcji większy bądź równy 0 - brak spełnienia warunków zadania", "Błąd!"
    else:
        xi = (a + b) / 2
        iteracje = 0

        if kryterium == "1":
            while not (abs(f(xi)) < epsilon):
                xi = xi - (f(xi) / df(xi))
                iteracje += 1

        else:
            while iteracje < epsilon:
                xi = xi - f(xi) / df(xi)
                iteracje += 1
    return xi, iteracje