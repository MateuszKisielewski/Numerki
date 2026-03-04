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
    stop_kryt()
    return a, b

def stop_kryt():
    print("Wybierz kryterium zatrzymania:")
    print("a. spełnienie warunku nałożonego na dokładność")
    print("b. osiągnięcie żądanej liczby iteracji")
    kryterium = input("Wybor: ")

    match kryterium:
        case "a":
            print("Wybrano a")
            podaj_epsilon()
        case "b":
            print("Wybrano b")
            podaj_iteracje()
        case _:
            print("Wybrano nieprawidłową literę!")

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
            zakres()
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