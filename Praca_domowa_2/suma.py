def suma(kolekcja: list | tuple | set | dict) -> int:
    suma = 0

    if isinstance(kolekcja, list | tuple | set):
        for element in kolekcja:
            if isinstance(element, int | float):
                suma += element

    elif isinstance(kolekcja, dict):
        for key, val in kolekcja.items():
            if isinstance(val, int | float):
                suma += val
    return suma


def test_suma():
    assert suma((1, 2, 3)) == 6
    assert suma((1, "2", 3)) == 4
    assert suma([8, 2, 3, 0, 8]) == 21
    assert suma([1, 2, "a"]) == 3
    assert suma({1: 8, 2: 2, 3: 3, 4: 0, 5: 9}) == 22
    assert suma({1: 8, 2: "a", 3: 3, 4: 0, 5: 9}) == 20


def suma_with_cast_to_int(
    kolekcja: list | tuple | set | dict, cast_to_int=False
) -> int:
    suma = 0
    if isinstance(kolekcja, list | tuple | set):
        for element in kolekcja:
            if isinstance(element, int | float):
                suma += element
            elif cast_to_int and isinstance(element, str):
                if element.isdecimal():
                    suma += int(element)

    elif isinstance(kolekcja, dict):
        for key, val in kolekcja.items():
            if isinstance(val, int | float):
                suma += val
            elif cast_to_int and isinstance(element, str):
                if val.isdecimal():
                    suma += int(val)
    return suma


print(suma({1: 8, 2: 2, 3: 3, 4: 0, 5: 9}))
print(suma_with_cast_to_int((1, "a", 3), cast_to_int=True))
test_suma()
