import math

stala_pi = 3.14159265358979323846

def kwadratura_gaussa(liczba_wezlow, funkcja):
    suma = 0.0
    waga = stala_pi / liczba_wezlow
    indeks = 1
    
    while indeks <= liczba_wezlow:
        argument_cosinusa = ((2.0 * indeks - 1.0) / (2.0 * liczba_wezlow)) * stala_pi
        wezel = math.cos(argument_cosinusa)
        suma += waga * funkcja(wezel)
        indeks += 1
        
    return suma

def funkcja_z_waga(argument, bazowa_funkcja):
    return bazowa_funkcja(argument) / math.sqrt(1.0 - argument * argument)

def calka_simpsona(poczatek, koniec, liczba_przedzialow, funkcja):
    szerokosc = (koniec - poczatek) / liczba_przedzialow
    suma = funkcja_z_waga(poczatek, funkcja) + funkcja_z_waga(koniec, funkcja)
    
    indeks = 1
    while indeks < liczba_przedzialow:
        argument = poczatek + indeks * szerokosc
        wartosc = funkcja_z_waga(argument, funkcja)
        
        czy_parzysta = (indeks % 2 == 0)
        if czy_parzysta:
            suma += 2.0 * wartosc
        else:
            suma += 4.0 * wartosc
        indeks += 1
        
    return suma * szerokosc / 3.0

def iteracyjny_simpson(poczatek, koniec, dokladnosc, funkcja):
    liczba_przedzialow = 2
    poprzedni_wynik = calka_simpsona(poczatek, koniec, liczba_przedzialow, funkcja)
    obecny_wynik = 0.0
    szukanie = True
    
    while szukanie:
        liczba_przedzialow *= 2
        obecny_wynik = calka_simpsona(poczatek, koniec, liczba_przedzialow, funkcja)
        
        osiagnieto_dokladnosc = (abs(obecny_wynik - poprzedni_wynik) < dokladnosc)
        if osiagnieto_dokladnosc:
            szukanie = False
        else:
            poprzedni_wynik = obecny_wynik
            
    return obecny_wynik

def oblicz_calke_wariant_1(dokladnosc, funkcja):
    calkowity_wynik = 0.0
    
    obecny_poczatek = 0.0
    szerokosc_kroku = 0.5
    obecny_koniec = obecny_poczatek + szerokosc_kroku
    szukanie_w_prawo = True
    
    while szukanie_w_prawo:
        wynik_czesciowy = iteracyjny_simpson(obecny_poczatek, obecny_koniec, dokladnosc, funkcja)
        calkowity_wynik += wynik_czesciowy
        
        prog_przekroczony = (abs(wynik_czesciowy) < dokladnosc)
        if prog_przekroczony:
            szukanie_w_prawo = False
        else:
            obecny_poczatek = obecny_koniec
            szerokosc_kroku *= 0.5
            obecny_koniec = obecny_poczatek + szerokosc_kroku
            
    obecny_koniec = 0.0
    szerokosc_kroku = 0.5
    obecny_poczatek = obecny_koniec - szerokosc_kroku
    szukanie_w_lewo = True
    
    while szukanie_w_lewo:
        wynik_czesciowy = iteracyjny_simpson(obecny_poczatek, obecny_koniec, dokladnosc, funkcja)
        calkowity_wynik += wynik_czesciowy
        
        prog_przekroczony = (abs(wynik_czesciowy) < dokladnosc)
        if prog_przekroczony:
            szukanie_w_lewo = False
        else:
            obecny_koniec = obecny_poczatek
            szerokosc_kroku *= 0.5
            obecny_poczatek = obecny_koniec - szerokosc_kroku
            
    return calkowity_wynik