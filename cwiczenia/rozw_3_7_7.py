from collections import Counter

zakupy = ["jajka", "mleko", "masło", "jajka", "chleb", "masło", "ser", "jajka"]


def zwroc_unikalne_produkty(zakupy: list) -> set:
    return set(zakupy)


def ilosc_wystapien_na_liscie(zakupy: list) -> dict[str, int]:
    # slownik ={}
    slownik = dict(Counter(zakupy))
    return slownik


print(zwroc_unikalne_produkty(zakupy))
ilosc_wystapien_na_liscie(zakupy)
