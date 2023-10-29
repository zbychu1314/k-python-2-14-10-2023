dane = "Anna 25, Tomasz 30, Ewa 28, Jan 35"


def przeksztalc_dane(dane: str) -> list:
    slownik = {}
    lista_osob = []
    lista_danych = dane.split(", ")
    for osoba in lista_danych:
        imie = osoba.split(" ")[0]
        wiek = osoba.split(" ")[1]
        slownik.update({imie: wiek})
    #print(slownik)
    lista_osob = [key for key, values in slownik.items() if int(values) > 30]
    print(lista_osob)
    return lista_osob


przeksztalc_dane(dane)
