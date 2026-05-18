import math
import numpy as np
import matplotlib.pyplot as plt
import math_utils

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
    
    for i in range(liczba_wezlow):
        wezel_znormalizowany = math.cos(math.pi * (2.0 * i + 1.0) / (2.0 * liczba_wezlow))
        wezel_przeskalowany = 0.5 * (koniec_przedzialu - poczatek_przedzialu) * wezel_znormalizowany + 0.5 * (poczatek_przedzialu + koniec_przedzialu)
        
        wartosc_funkcji = ewaluuj_funkcje(numer_funkcji, wezel_przeskalowany)
        
        for k in range(stopien_wielomianu + 1):
            wartosc_wielomianu_czebyszewa = math.cos(k * math.pi * (2.0 * i + 1.0) / (2.0 * liczba_wezlow))
            wspolczynniki_calkowe[k] += wartosc_funkcji * wartosc_wielomianu_czebyszewa
            
    wspolczynniki_calkowe[0] = wspolczynniki_calkowe[0] / liczba_wezlow
    for k in range(1, stopien_wielomianu + 1):
        wspolczynniki_calkowe[k] = (2.0 * wspolczynniki_calkowe[k]) / liczba_wezlow
        
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

def generuj_wykres(numer_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu, stopien_wielomianu, obliczony_blad):
    liczba_punktow_wykresu = 500
    punkty_na_osi_x = np.linspace(poczatek_przedzialu, koniec_przedzialu, liczba_punktow_wykresu)
    
    wartosci_oryginalne = []
    for punkt_x in punkty_na_osi_x:
        wartosci_oryginalne.append(ewaluuj_funkcje(numer_funkcji, punkt_x))
    
    wartosci_aproksymacji = []
    for punkt_x in punkty_na_osi_x:
        punkt_znormalizowany = (2.0 * punkt_x - poczatek_przedzialu - koniec_przedzialu) / (koniec_przedzialu - poczatek_przedzialu)
        wartosci_aproksymacji.append(math_utils.horner(punkt_znormalizowany, wspolczynniki_potegowe, len(wspolczynniki_potegowe)))
        
    plt.figure(figsize=(10, 6))
    plt.plot(punkty_na_osi_x, wartosci_oryginalne, label="Funkcja oryginalna", color='blue', linewidth=2)
    plt.plot(punkty_na_osi_x, wartosci_aproksymacji, label=f"Aproksymacja (stopien {stopien_wielomianu})", color='red', linestyle='--')
    
    plt.title(f"Aproksymacja Czebyszewa | RMSE: {round(obliczony_blad, 6)}")
    plt.xlabel("os X")
    plt.ylabel("wartosc funkcji")
    plt.legend()
    plt.grid(True)
    plt.show()

def uruchom_program():
    while True:
        print("\nAPROKSYMACJA SREDNIOKWADRATOWA (CZEBYSZEW)")
        print("1. Funkcja liniowa: 2x - 3")
        print("2. Funkcja modul: |x|")
        print("3. Wielomian: 2x^3 - 4x^2 + x - 5")
        print("4. Funkcja trygonometryczna: sin(x)")
        print("5. Zlozenie funkcji: sin(|x|)")
        print("0. Wyjscie")
        
        wybor_uzytkownika = input("Wybierz funkcję: ")
        if wybor_uzytkownika == '0': 
            break
            
        numer_wybranej_funkcji = int(wybor_uzytkownika)
        if 1 <= numer_wybranej_funkcji <= 5:
            poczatek_przedzialu = float(input("Podaj poczatek przedzialu (a): "))
            koniec_przedzialu = float(input("Podaj koniec przedzialu (b): "))
            
            if poczatek_przedzialu >= koniec_przedzialu:
                print("Blad: wartosc poczatku musi byc mniejsza od konca przedzialu!")
                continue
                
            liczba_wezlow_calkowania = int(input("Podaj liczbe wezlow calkowania Gaussa (np. 100): "))
            
            print("\nWybierz tryb pracy:")
            print("1. Standardowy (podaje z gory stopien wielomianu)")
            print("2. Zaawansowany - ocena 5.0 (iteracyjny dobor stopnia do zadanego bledu)")
            wybrany_tryb = input("Wybor: ")
            
            if wybrany_tryb == '1':
                stopien_aproksymacji = int(input("Podaj stopien wielomianu aproksymacyjnego: "))
                wspolczynniki_potegowe = wspolczynniki_dla_hornera(numer_wybranej_funkcji, poczatek_przedzialu, koniec_przedzialu, stopien_aproksymacji, liczba_wezlow_calkowania)
                obliczony_blad = oblicz_blad(numer_wybranej_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu)
                
                print(f"\nBlad aproksymacji (RMSE): {round(obliczony_blad, 6)}")
                generuj_wykres(numer_wybranej_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu, stopien_aproksymacji, obliczony_blad)
                
            elif wybrany_tryb == '2':
                docelowy_blad = float(input("Podaj akceptowalny blad (np. 0.01): "))
                maksymalny_stopien = 40
                czy_osiagnieto_cel = False
                
                for obecny_stopien in range(1, maksymalny_stopien + 1):
                    bezpieczna_liczba_wezlow = max(liczba_wezlow_calkowania, obecny_stopien + 10) 
                    wspolczynniki_potegowe = wspolczynniki_dla_hornera(numer_wybranej_funkcji, poczatek_przedzialu, koniec_przedzialu, obecny_stopien, bezpieczna_liczba_wezlow)
                    obliczony_blad = oblicz_blad(numer_wybranej_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu)
                    
                    if obliczony_blad <= docelowy_blad:
                        print(f"\nSukces! Osiagnieto wymagany blad: {round(obliczony_blad, 6)} dla wielomianu stopnia = {obecny_stopien}")
                        generuj_wykres(numer_wybranej_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu, obecny_stopien, obliczony_blad)
                        czy_osiagnieto_cel = True
                        break
                        
                if not czy_osiagnieto_cel:
                    print(f"\nNie udalo sie osiagnac zadanego bledu w maksymalnym stopniu ({maksymalny_stopien}).")
                    print(f"Najlepszy uzyskany blad: {round(obliczony_blad, 6)} (dla stopnia = {maksymalny_stopien})")
                    generuj_wykres(numer_wybranej_funkcji, wspolczynniki_potegowe, poczatek_przedzialu, koniec_przedzialu, maksymalny_stopien, obliczony_blad)
            else:
                print("Niepoprawny tryb!")
        else:
            print("Niepoprawny wybor funkcji!")

uruchom_program()