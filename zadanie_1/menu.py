from algorytmy import f_wielomian, bisekcja, styczna, df_wielomian

def menu():
    print("Wybierz jedną z funkcji:")
    print("1. Wielomian: f(x) = 1*x^3 + 2*x^2 - 1*x - 2")
    print("2. Trygonometryczna: f(x) = cos(x) - 0.5")
    print("3. Wykładnicza: f(x) = e^x - 7")
    print("4. Złożenia: f(x) = x^3 - cos(x) - e^x + 7")
    f=input("Wybor: ")

    match f:
        case "1":
            print("Wybrano wielomian f(x) = 1*x^3 + 2*x^2 - 1*x - 2")
        case "2":
            print("Wybrano trygonometryczną f(x) = cos(x) - 0.5")
        case "3":
            print("Wybrano wykładniczą f(x) = e^x - 7")
        case "4":
            print("Wybrano Złożenia f(x) = x^3 - cos(x) - e^x + 7")
        case _:
            print("Podano niepoprawną cyfrę!\n")
            menu()

def zakres():
    print("Podaj zakres")
    a = int(input("A: "))
    b = int(input("B: "))
    kryterium, wartosc = stop_kryt()
    return a, b, kryterium, wartosc

def stop_kryt():
    print("Wybierz kryterium zatrzymania:")
    print("1. spełnienie warunku nałożonego na dokładność")
    print("2. osiągnięcie żądanej liczby iteracji")
    kryterium = input("Wybor: ")

    match kryterium:
        case "1":
            print("Wybrano 1")
            epsilon = podaj_epsilon()
            return '1', epsilon
        case "2":
            print("Wybrano 2")
            iteracja = podaj_iteracje()
            return '2', iteracja
        case _:
            print("Wybrano nieprawidłowo!")
            stop_kryt()

def podaj_epsilon():
    epsilon = float(input("Podaj epsilon: "))
    return epsilon

def podaj_iteracje():
    iteracje = int(input("Podaj liczbę iteracji: "))
    return iteracje

def wariant():
    print("Wybierz wariant:")
    print("1. Bisekcja")
    print("2. Metoda stycznych")
    wybrany_wariant = input("Wybor: ")
    match wybrany_wariant:
        case "1":
            print("Wybrano bisekcję")
            return "bisekcja"
        case "2":
            print("Wybrano metodę stycznych")       
            return "styczna"
        case _: 
            print("Wybrano nieprawidłowo!")
            wariant()

wybor = "T"
while wybor != 'N':
        if wybor == 'T':
            menu()
            a, b, kryterium, wartosc = zakres()
            wariant_do_obliczen = wariant()
            if wariant == "bisekcja":
                wynik, iteracje = bisekcja(f_wielomian, a, b, kryterium, wartosc)
            else:
                wynik, iteracje = styczna(f_wielomian, df_wielomian, a, b, kryterium, wartosc)
            print("wynik: ", wynik)
            print("iteracje: ", iteracje)
            wybor = input("Czy chcesz korzystać z programu?(T/N): ")

# Trzeba zrobić funkcje dla pozostałych 3 funkcji, a następnie dodać je do menu i algorytmów, estetyka kodu, oraz dodać obsługę błędów: zły zakres, zły wybór wariantu, zły wybór kryterium