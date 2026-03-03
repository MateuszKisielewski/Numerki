#menu
def menu():
    print("Wybierz jedną z funkcji:")
    print("1. Wielomian")
    print("2. Trygonometryczna")
    print("3. Wykładnicza")
    print("4. Złożenia")
    print("0. Wyjdź")

def zakres():
    print("Podaj zakres")
    print("A:")
    A = input()
    print("B:")
    B = input()
    stop_kryt()

def stop_kryt():
    print("Wybierz kryterium zatrzymania:")
    print("a. spełnienie warunku nałożonego na dokładność")
    print("b. osiągnięcie żądanej liczby iteracji")
    kryterium = input()

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
    print("Podaj epsilon:")
    epsilon = input()

def podaj_iteracje():
    print("Podaj liczbę iteracji:")
    iteracje = input()

while True:
    menu()
    wybor = input("Podaj cyfrę: ")

    match wybor:
        case "1":
            print("Wybrano wielomian")
            zakres()
            break
        case "2":
            print("Wybrano trygonometryczną")
            zakres()
            break
        case "3":
            print("Wybrano wykładniczą")
            zakres()
            break
        case "4":
            print("Wybrano Złożenia")
            zakres()
            break
        case "0":
            print("Zamknięto program")
            break
        case _:
            print("Podano niepoprawną cyfrę!\n")