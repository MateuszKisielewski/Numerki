def rozwiaz_uklad_gaussa(macierz_a, wektor_b):
    n = len(macierz_a)

    macierz_roz = [wiersz[:] + [b_i] for wiersz, b_i in zip(macierz_a, wektor_b)]
    eps = 0.000001

    for i in range(n):
        max_indeks = i
        for k in range(i + 1, n):
            if abs(macierz_roz[k][i]) > abs(macierz_roz[max_indeks][i]):
                max_indeks = k

        if max_indeks != i:
            macierz_roz[i], macierz_roz[max_indeks] = macierz_roz[max_indeks], macierz_roz[i]

        if abs(macierz_roz[i][i]) >= eps:
            for j in range(i + 1, n):
                mnoznik = macierz_roz[j][i] / macierz_roz[i][i]
                for k in range(i, n + 1):
                    macierz_roz[j][k] -= mnoznik * macierz_roz[i][k]

    typ_ukladu = "oznaczony"
    for i in range(n):
        czy_wiersz_zerowy = True
        for j in range(n):
            if abs(macierz_roz[i][j]) >= eps:
                czy_wiersz_zerowy = False
                
        wyraz_wolny = macierz_roz[i][n]
        
        if czy_wiersz_zerowy:
            if abs(wyraz_wolny) >= eps:
                return None, "sprzeczny"
            else:
                typ_ukladu = "nieoznaczony"
                
    if typ_ukladu == "nieoznaczony":
        return None, "nieoznaczony"

    wynik = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += macierz_roz[i][j] * wynik[j]
        wynik[i] = (macierz_roz[i][n] - suma) / macierz_roz[i][i]
        
    return wynik, "oznaczony"