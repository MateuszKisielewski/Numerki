def wczytaj_uklad_z_pliku(nazwa_pliku, liczba_rownan):
    macierz_a = []
    wektor_b = []
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            linie = plik.readlines()
            
            if len(linie) < liczba_rownan:
                print(f"Błąd: Plik zawiera za mało wierszy")
                return None, None
                
            for i in range(liczba_rownan):
                wspolczynniki = []
                kawalki_tekstu = linie[i].strip().split()
                for x in kawalki_tekstu:
                     liczba = float(x)
                     wspolczynniki.append(liczba)
                     
                if len(wspolczynniki) != liczba_rownan + 1:
                    print(f"Błąd w wierszu {i+1}: zła liczba współczynników")
                    return None, None
                
                macierz_a.append(wspolczynniki[:-1])
                wektor_b.append(wspolczynniki[-1])
                
        return macierz_a, wektor_b
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{nazwa_pliku}'")
        return None, None
    except ValueError:
        print("Błąd: Plik zawiera nieprawidłowe dane")
        return None, None