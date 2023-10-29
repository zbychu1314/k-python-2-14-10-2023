def znajdz_pozycje(lista:list,liczba:int)->list:
    lista_indeksow =[]
    indeks_start = 0
    for number in lista:
        if number == liczba:
            index_number=lista.index(number,indeks_start,len(lista))
            lista_indeksow.append(index_number)
        indeks_start +=1
        print()
    print(lista_indeksow)

lista = [2, 3, 1, 25, 6, 1, 232, 34, 1, 232]
znajdz_pozycje(lista,1)