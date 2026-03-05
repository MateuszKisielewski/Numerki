from horner import horner

def f_wielomian(x):
    return horner(x, [1, 0, -1, -2], 4)

def bisekcja(f, a, b, kryterium, epsilon):
    if  f(a) * f(b) >= 0:
        return "iloczyn funkcji większy bądź równy 0 - brak spełnienia warunków zadania"
    else:
        xi = (a + b) / 2
        iteracje = 0

        if kryterium == "1":
            while not (abs(f_wielomian(xi)) < epsilon):
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
                xi = (a + b) / 2
                iteracje += 1

        else:
            while iteracje < epsilon:
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
                xi = (a + b) / 2
                iteracje += 1
    return xi, iteracje

def styczna(f, df, a, b, kryterium, epsilon):
    if f(a) * f(b) >= 0:
        return "iloczyn funkcji większy bądź równy 0 - brak spełnienia warunków zadania"
    else:
        xi = (a + b) / 2
        iteracje = 0

        if kryterium == "1":
            while not (abs(f_wielomian(xi)) < epsilon):
                xi = xi - (f(xi) / df(xi))
                iteracje += 1

        else:
            while iteracje < epsilon:
                xi = xi - f(xi) / df(xi)
                iteracje += 1
    return xi, iteracje
