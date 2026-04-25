import matplotlib.pyplot as plt
import functions
import interpolation


def generuj_wykres(id_funkcji, a, b, n):
    wezly_x = interpolation.generuj_wezly_czebyszewa(a, b, n)
    wezly_y = []

    i = 0
    while i < n:
        y = functions.ewaluuj_funkcje(id_funkcji, wezly_x[i])
        wezly_y.append(y)
        i += 1

    liczba_punktow_wykresu = 500
    krok = (b - a) / (liczba_punktow_wykresu - 1)

    X_plot = []
    Y_oryginalna = []
    Y_interpolacja = []

    j = 0
    while j < liczba_punktow_wykresu:
        x_curr = a + j * krok
        X_plot.append(x_curr)

        Y_oryginalna.append(functions.ewaluuj_funkcje(id_funkcji, x_curr))

        y_interp = interpolation.lagrange_oblicz_wartosc(x_curr, wezly_x, wezly_y, n)
        Y_interpolacja.append(y_interp)

        j += 1

    plt.figure(figsize=(10, 6))
    plt.plot(X_plot, Y_oryginalna, label="Funkcja oryginalna", color='blue', linewidth=2)
    plt.plot(X_plot, Y_interpolacja, label="Wielomian interpolacyjny", color='red', linestyle='--')
    plt.plot(wezly_x, wezly_y, 'ko', label="Węzły interpolacji (Czebyszewa)")

    plt.title("Interpolacja Lagrange'a na węzłach Czebyszewa")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


def uruchom_program():
    dziala = True
    while dziala:
        print("\nMENU INTERPOLACJI")
        print("1. Funkcja liniowa: (2x - 3)")
        print("2. Funkcja z wartością bezwzględną: |x|")
        print("3. Wielomian: (2x^3 - 4x^2 + x - 5)")
        print("4. Funkcja trygonometryczna: (sin(x))")
        print("5. Złożenie funkcji: (sin(|x|))")
        print("0. Wyjście z programu")

        wybor_str = input("Wybierz funkcję: ")

        if wybor_str == '0':
            dziala = False
        else:
            id_funkcji = int(wybor_str)
            if 1 <= id_funkcji <= 5:
                a = float(input("Podaj początek przedziału (a): "))
                b = float(input("Podaj koniec przedziału (b): "))
                n = int(input("Podaj liczbę węzłów (n > 0): "))

                if n > 0 and a < b:
                    generuj_wykres(id_funkcji, a, b, n)
                else:
                    print("Błędne dane przedziału lub liczby węzłów")
            else:
                print("Niepoprawny wybór funkcji")


if __name__ == "__main__":
    uruchom_program()