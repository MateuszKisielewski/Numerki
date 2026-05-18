import math
import numpy as np
import matplotlib.pyplot as plt
import math_utils
from calkowanie_zadanie_4 import kwadratura_gaussa

def f_liniowa(punkt_x):
    return 2.0 * punkt_x - 3.0

def f_modul(punkt_x):
    return abs(punkt_x)

def f_wielomian(punkt_x):
    wspolczynniki_bazowe = [2.0, -4.0, 1.0, -5.0]
    return math_utils.horner(punkt_x, wspolczynniki_bazowe, len(wspolczynniki_bazowe))

def f_trygonometryczna(punkt_x):
    return math.sin(punkt_x)

def f_zlozenie(punkt_x):
    return math.sin(abs(punkt_x))

def ewaluuj_funkcje(numer_funkcji, punkt_x):
    if numer_funkcji == 1:
        return f_liniowa(punkt_x)
    elif numer_funkcji == 2:
        return f_modul(punkt_x)
    elif numer_funkcji == 3:
        return f_wielomian(punkt_x)
    elif numer_funkcji == 4:
        return f_trygonometryczna(punkt_x)
    elif numer_funkcji == 5:
        return f_zlozenie(punkt_x)
    return 0.0

def wyznacz_wspolczynniki_czebyszewa(stopien_wielomianu):
    macierz_wspolczynnikow = []
    for i in range(stopien_wielomianu + 1):
        nowy_wiersz = [0.0] * (stopien_wielomianu + 1)
        macierz_wspolczynnikow.append(nowy_wiersz)
        
    macierz_wspolczynnikow[0][0] = 1.0
    if stopien_wielomianu > 0:
        macierz_wspolczynnikow[1][1] = 1.0
        
    for k in range(2, stopien_wielomianu + 1):
        for j in range(k + 1):
            if j > 0:
                pierwszy_skladnik = 2.0 * macierz_wspolczynnikow[k-1][j-1]
            else:
                pierwszy_skladnik = 0.0
                
            if j < k:
                drugi_skladnik = macierz_wspolczynnikow[k-2][j]
            else:
                drugi_skladnik = 0.0
                
            macierz_wspolczynnikow[k][j] = pierwszy_skladnik - drugi_skladnik
            
    return macierz_wspolczynnikow

def calkowanie_gaussa_czebyszewa(numer_funkcji, poczatek_przedzialu, koniec_przedzialu, stopien_wielomianu, liczba_wezlow):
    wspolczynniki_calkowe = [0.0] * (stopien_wielomianu + 1)
    
    def przeskaluj_x(x):
        return 0.5 * (koniec_przedzialu - poczatek_przedzialu) * x + 0.5 * (poczatek_przedzialu + koniec_przedzialu)
        
    for k in range(stopien_wielomianu + 1):
        
        def funkcja_podcalkowa(x):
            wartosc_wielomianu_czebyszewa = math.cos(k * math.acos(x))
            wartosc_funkcji = ewaluuj_funkcje(numer_funkcji, przeskaluj_x(x))
            return wartosc_funkcji * wartosc_wielomianu_czebyszewa
            
        wartosc_calki = kwadratura_gaussa(liczba_wezlow, funkcja_podcalkowa)
        
        if k == 0:
            wspolczynniki_calkowe[k] = (1.0 / math.pi) * wartosc_calki
        else:
            wspolczynniki_calkowe[k] = (2.0 / math.pi) * wartosc_calki
            
    return wspolczynniki_calkowe

def wspolczynniki_dla_hornera(numer_funkcji, poczatek_przedzialu, koniec_przedzialu, stopien_wielomianu, liczba_wezlow):
    wspolczynniki_calkowe = calkowanie_gaussa_czebyszewa(numer_funkcji, poczatek_przedzialu, koniec_przedzialu, stopien_wielomianu, liczba_wezlow)
    macierz_czebyszewa = wyznacz_wspolczynniki_czebyszewa(stopien_wielomianu)
    
    wspolczynniki_potegowe = [0.0] * (stopien_wielomianu + 1)
    for j in range(stopien_wielomianu + 1):
        for k in range(j, stopien_wielomianu + 1):
            wspolczynniki_potegowe[j] += wspolczynniki_calkowe[k] * macierz_czebyszewa[k][j]
            
    wspolczynniki_potegowe.reverse()
    return wspolczynniki_potegowe

def oblicz_blad(numer_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu, liczba_punktow_testowych=1000):
    suma_kwadratow_bledow = 0.0
    krok_przedzialu = (koniec_przedzialu - poczatek_przedzialu) / (liczba_punktow_testowych - 1)
    
    for i in range(liczba_punktow_testowych):
        punkt_x = poczatek_przedzialu + i * krok_przedzialu
        punkt_znormalizowany = (2.0 * punkt_x - poczatek_przedzialu - koniec_przedzialu) / (koniec_przedzialu - poczatek_przedzialu)
        
        wartosc_aproksymowana = math_utils.horner(punkt_znormalizowany, wspolczynniki_potegowe, len(wspolczynniki_potegowe))
        wartosc_dokladna = ewaluuj_funkcje(numer_funkcji, punkt_x)
        
        suma_kwadratow_bledow += (wartosc_aproksymowana - wartosc_dokladna)**2
        
    return math.sqrt(suma_kwadratow_bledow / liczba_punktow_testowych)