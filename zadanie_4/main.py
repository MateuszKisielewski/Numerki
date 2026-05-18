from funkcje import funkcja_wielomianowa, funkcja_trygonometryczna, funkcja_wykladnicza
from calkowanie import kwadratura_gaussa, oblicz_calke_wariant_1

def wyswietl_wyniki(wybrana_funkcja, wzor_funkcji, dokladnosc):
    print(f"Całkowana funkcja bazowa f(x) = {wzor_funkcji}")
    print(f"Pełna postać w całce: w(x) * f(x) = (1 / sqrt(1 - x^2)) * ({wzor_funkcji})")
    
    print(f"Kwadratura Gaussa (2 wezly): {kwadratura_gaussa(2, wybrana_funkcja):.6f}")
    print(f"Kwadratura Gaussa (3 wezly): {kwadratura_gaussa(3, wybrana_funkcja):.6f}")
    print(f"Kwadratura Gaussa (4 wezly): {kwadratura_gaussa(4, wybrana_funkcja):.6f}")
    print(f"Kwadratura Gaussa (5 wezly): {kwadratura_gaussa(5, wybrana_funkcja):.6f}")
    
    wynik_newtona = oblicz_calke_wariant_1(dokladnosc, wybrana_funkcja)
    print(f"Zlozona Kwadratura Newtona-Cotesa: {wynik_newtona:.6f}\n")

def glowna():
    tekst_dokladnosci = input("Podaj zadana dokladność obliczeń: ")
    zadana_dokladnosc = float(tekst_dokladnosci)
    
    wybor = "0"
    while wybor != "4":
        print("Wybierz funkcje podcałkową:")
        print("1. Funkcja wielomianowa: 2x^3 - 3x^2 + x + 5")
        print("2. Funkcja trygonometryczna: cos(x) + 2")
        print("3. Funkcja wykładnicza: e^x")
        print("4. Wyjście z programu")
        
        wybor = input("Twoj wybor: ")
        
        if wybor == "1":
            wyswietl_wyniki(funkcja_wielomianowa, "2x^3 - 3x^2 + x + 5", zadana_dokladnosc)
        elif wybor == "2":
            wyswietl_wyniki(funkcja_trygonometryczna, "cos(x) + 2", zadana_dokladnosc)
        elif wybor == "3":
            wyswietl_wyniki(funkcja_wykladnicza, "e^x", zadana_dokladnosc)
        elif wybor != "4":
            print("Niepoprawny wybor, spróbuj ponownie\n")

if __name__ == "__main__":
    glowna()