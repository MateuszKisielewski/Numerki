from algorytmy import f_wielomian, bisekcja


def menu():
    print("Wybierz jedną z funkcji:")
    print("1. Wielomian")
    print("2. Trygonometryczna")
    print("3. Wykładnicza")
    print("4. Złożenia")
    print("0. Wyjdź")

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
            print("Wybrano nieprawidłową literę!")
            stop_kryt()

def podaj_epsilon():
    epsilon = float(input("Podaj epsilon: "))
    return epsilon

def podaj_iteracje():
    iteracje = int(input("Podaj liczbę iteracji: "))
    return iteracje

wybor = ""
while wybor != "0":
    menu()
    wybor = input("Podaj cyfrę: ")

    match wybor:
        case "1":
            print("Wybrano wielomian")
            a, b, kryterium, wartosc = zakres()
            wynik, iteracje = bisekcja(f_wielomian, a, b, kryterium, wartosc)
            print("wynik: ", wynik)
            print("iteracje: ", iteracje)
        case "2":
            print("Wybrano trygonometryczną")
            zakres()
        case "3":
            print("Wybrano wykładniczą")
            zakres()
        case "4":
            print("Wybrano Złożenia")
            zakres()
        case "0":
            print("Zamknięto program")
        case _:
            print("Podano niepoprawną cyfrę!\n")