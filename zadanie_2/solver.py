def rozwiaz_uklad_gaussa(macierz_a, wektor_b):
    n = len(macierz_a)
    
    # Tworzenie macierzy rozszerzonej
    macierz_roz = [wiersz[:] + [b_i] for wiersz, b_i in zip(macierz_a, wektor_b)]
    eps = 1e-10  # Tolerancja dla zera zmiennoprzecinkowego
    
    # Krok eliminacji w przód
    for i in range(n):
        # 1. Wybór elementu podstawowego (częściowe osiowanie)
        max_indeks = i
        for k in range(i + 1, n):
            if abs(macierz_roz[k][i]) > abs(macierz_roz[max_indeks][i]):
                max_indeks = k
                
        # Zamiana wierszy, jeśli największy element jest w innym wierszu
        if max_indeks != i:
            macierz_roz[i], macierz_roz[max_indeks] = macierz_roz[max_indeks], macierz_roz[i]
            
        # 2. Eliminacja zmiennych - wykonujemy TYLKO jeśli element główny nie jest zerem
        # Wcześniej było tutaj 'continue', teraz zmieniliśmy to na bezpieczny warunek if
        if abs(macierz_roz[i][i]) >= eps:
            for j in range(i + 1, n):
                mnoznik = macierz_roz[j][i] / macierz_roz[i][i]
                for k in range(i, n + 1):
                    macierz_roz[j][k] -= mnoznik * macierz_roz[i][k]
                
    # 3. Analiza rozwiązań (sprawdzanie od dołu)
    typ_ukladu = "oznaczony"
    for i in range(n):
        # Sprawdzamy czy cała lewa strona równania to zera
        czy_wiersz_zerowy = True
        for j in range(n):
            if abs(macierz_roz[i][j]) >= eps:
                czy_wiersz_zerowy = False
                # Pętla bez 'break', przeszuka do końca, ale to zgodne z zasadami
                
        wyraz_wolny = macierz_roz[i][n]
        
        if czy_wiersz_zerowy:
            if abs(wyraz_wolny) >= eps:
                # 0 = liczba (np. 0 = 5) -> Sprzeczność
                return None, "sprzeczny"
            else:
                # 0 = 0 -> Nieskończenie wiele rozwiązań
                typ_ukladu = "nieoznaczony"
                
    if typ_ukladu == "nieoznaczony":
        return None, "nieoznaczony"
        
    # 4. Postępowanie odwrotne (Back substitution)
    wynik = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += macierz_roz[i][j] * wynik[j]
        wynik[i] = (macierz_roz[i][n] - suma) / macierz_roz[i][i]
        
    return wynik, "oznaczony"