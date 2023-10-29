def czy_ujemna(lista:list):
    for wartosc in lista:
        czy_ujemna =False
        if wartosc < 0:
            czy_ujemna =True
        if wartosc > 0:
            return None
        print(wartosc)
        return wartosc

testowa_lista = [1,2,3,4,-3]
testowa_lista2 = [-1,2,3,4]
assert czy_ujemna(testowa_lista2) == -1
assert czy_ujemna(testowa_lista) is None
print(czy_ujemna(testowa_lista))
#print((min(testowa_lista)))
#
#def zwroc_index(lista:list):
#    najmniejsza = min(lista)
#    najwieksza = max(lista)
#    return testowa_lista.index(najmniejsza), testowa_lista.index(najwieksza)
#
#print(zwroc_index(testowa_lista))
#
#assert zwroc_index(testowa_lista2) == 0,3