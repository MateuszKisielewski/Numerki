from file_manager import wczytaj_uklad_z_pliku
from solver import rozwiaz_uklad_gaussa

def uruchom():
    print("--- ROZWIĄZYWANIE UKŁADU RÓWNAŃ METODĄ ELIMINACJI GAUSSA ---")
    try:
        liczba_rownan = int(input("Podaj liczbę równań (N): "))
        if liczba_rownan <= 0:
            print("Liczba równań musi być większa od zera!")
            return
            
        nazwa_pliku = input("Podaj nazwę pliku z macierzą (np. uklad.txt): ")
        
        macierz_a, wektor_b = wczytaj_uklad_z_pliku(nazwa_pliku, liczba_rownan)
        
        if macierz_a is not None and wektor_b is not None:
            print("\nWczytany układ równań pomyślnie. Trwa obliczanie...")
            wynik, status = rozwiaz_uklad_gaussa(macierz_a, wektor_b)
            
            print("\n--- WYNIK ---")
            if status == "oznaczony":
                print("Układ jest oznaczony (posiada jedno rozwiązanie):")
                for i, x in enumerate(wynik):
                    print(f"x_{i+1} = {x:.6f}")
            elif status == "sprzeczny":
                print("Układ jest sprzeczny (nie posiada rozwiązań).")
            elif status == "nieoznaczony":
                print("Układ jest nieoznaczony (posiada nieskończenie wiele rozwiązań).")
                
    except ValueError:
        print("Nieprawidłowa wartość! Proszę podać liczbę całkowitą.")

if __name__ == "__main__":
    uruchom()