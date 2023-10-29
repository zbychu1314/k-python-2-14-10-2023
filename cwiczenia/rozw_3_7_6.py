osoby = [
    {'imie': 'Anna', 'wiek': 28, 'zawod': 'inżynier'},
    {'imie': 'Tomasz', 'wiek': 35, 'zawod': 'lekarz'},
    {'imie': 'Karolina', 'wiek': 40, 'zawod': 'nauczyciel'},
    {'imie': 'Pawel', 'wiek': 40, 'zawod': 'nauczyciel'},
    {'imie': 'Karol', 'wiek': 42, 'zawod': 'programista'},
    {'imie': 'Piotr', 'wiek': 32, 'zawod': 'programista'}

]

def zwroc_slownik(osoby:list)->dict:
    slownik_osoby={}
    try:
        lista_zawodow = [zawod['zawod'] for zawod in osoby]
        lista_zawodow=list(set(lista_zawodow))
        print(f'Lista zawodow: {lista_zawodow}')

        for zawod in lista_zawodow:
            lista_temp = [osoba['imie'] for osoba in osoby if osoba['zawod'] == zawod]
            print(f'Lista osob {zawod}: {lista_temp}')
            slownik_osoby.update({zawod:lista_temp})
        print(slownik_osoby)
    except KeyError:
        print('KeyNotFound')
    return slownik_osoby

zwroc_slownik(osoby)

