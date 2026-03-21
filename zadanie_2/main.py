def menu():
    while True:
        print("1. Wprowadź dane ręcznie")
        print("2. Wczytaj dane z pliku")
        print("3. Wyświetl aktualny układ")
        print("4. Rozwiąż układ")
        print("0. Wyjście")

        wybor = input("Wybierz opcję: ")

        match wybor:
            case "1":
                print("Wybrano: wprowadź dane ręcznie")
            case "2":
                print("Wybrano: wczytaj dane z pliku")
            case "3":
                print("Wybrano: wyświetl aktualny układ")
            case "4":
                print("Wybrano: rozwiąż układ")
            case "0":
                print("Koniec programu")
            case _:
                print("Nieprawidłowa opcja")

menu()