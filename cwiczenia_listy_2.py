def usun_liczby_z_listy(lista:list)->None:
    lista_pomocnicza =[]
    lista_pomocnicza=lista
    for liczba in lista:
        if liczba%2 == 0:
            lista_pomocnicza.remove(liczba)
    lista = lista_pomocnicza
    #print(lista)

lista = [1,2,3,4,5,6,7,8]
print(id(lista))
assert usun_liczby_z_listy(lista) is None
assert lista == [1, 3, 5, 7]
#usun_liczby_z_listy(lista)
print(id(lista))
