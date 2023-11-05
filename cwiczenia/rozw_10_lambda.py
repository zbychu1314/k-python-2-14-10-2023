from typing import Callable, Union, List
Collection = str or List



def wytnij(liczby:Collection,*,start:Callable,stop:Callable) ->  Collection:
    #liczby = sorted(liczby)
    found_a=False
    found_b=False
    for liczba in liczby:
        print(liczba)
        wynik_a=(start(liczba))
        wynik_b=(stop(liczba))
        if wynik_a is True and found_a is False:
            index_a=liczby.index(liczba)
            found_a=True
        elif wynik_b is True and found_b is False:
            index_b=liczby.index(liczba)
            found_b=True
    return liczby[index_a:index_b]

liczby = [ 2, 3, 5, 10, 46, 73, 90]
znaki="12312456078"

#print(wytnij(liczby,start=lambda x: True if x >5 else False,stop=lambda y: True if y >70 else False))
print(wytnij(znaki,start=lambda x: x=='3',stop=lambda y:y=='7'))
