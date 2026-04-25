# interpolation.py
import math

def generuj_wezly_czebyszewa(a, b, n):
    """Generuje n węzłów Czebyszewa na przedziale [a, b]."""
    wezly = []
    i = 0
    while i < n:
        # Wzór na węzły Czebyszewa
        argument_cos = math.pi * (2.0 * i + 1.0) / (2.0 * n)
        pierwiastek = math.cos(argument_cos)
        x_i = 0.5 * (a + b) + 0.5 * (b - a) * pierwiastek
        wezly.append(x_i)
        i += 1
    return wezly

def lagrange_oblicz_wartosc(x, wezly_x, wezly_y, n):
    """
    Oblicza wartość wielomianu interpolacyjnego bezpośrednio ze wzoru Lagrange'a.
    Nie stosujemy tu schematu Hornera (zgodnie z poleceniem).
    """
    wynik = 0.0
    i = 0
    while i < n:
        term = wezly_y[i]
        j = 0
        while j < n:
            # Zamiast 'continue', które jest zakazane, używamy warunku logicznego
            if i != j:
                term = term * (x - wezly_x[j]) / (wezly_x[i] - wezly_x[j])
            j += 1
        wynik += term
        i += 1
    return wynik