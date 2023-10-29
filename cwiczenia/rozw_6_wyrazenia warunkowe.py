def zwroc_ocene()->str:
    while True:
        wynik = input('Podaj liczbe:')
        if not wynik.isalpha():
            wynik =int(wynik)
            if wynik in range(90,100):
                return 'A'
            elif wynik in range(80,90):
                return 'B'
            elif wynik in range(70,80):
                return 'C'
            elif wynik in range(60,70):
                return 'D'
            elif wynik in range(50,60):
                return 'E'
            elif wynik in range(0,50):
                return 'F'
            else:
                return None

print(zwroc_ocene())