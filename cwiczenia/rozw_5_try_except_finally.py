def podziel_wartosci():
    wprowadz_ponownie = True
    while wprowadz_ponownie:
        liczba_a=input('Podaj liczbe a:')
        liczba_b=input('Podaj liczbe b:')
        try:
            wynik=float(liczba_a)/float(liczba_b)
            wprowadz_ponownie = False
            return wynik
        except ZeroDivisionError:
            print("Blad próbujesz dzielić przez zero")
            wprowadz_ponownie = False
        except ValueError:
            print('Wprowadziles niepoprawne dane, wprowadź ponownie!')
        except Exception as e:
            print(f'Wystapil nieoczekiwany blad {e}')
        finally:
            print("Koniec programu")
#### ew mozna to zrobic break
print(podziel_wartosci())

