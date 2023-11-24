def pascal_triangle(n:int, to_str = False)->list[list[int]]:
    i = 0
    tablica = []
    while i < n:
        if not tablica:
            tablica.append([1])
            i+=1
        elif len(tablica) == 1:
            tablica.append([1,1])
            i+=1
        else:
            elems = []
            for j in range(0,len(tablica[i-1])-1):                
                elems.append(tablica[i-1][j]+tablica[i-1][j+1])
            tablica.append([1])
            for elem in elems:
                tablica[i].append(elem)
            tablica[i].append(1)
            i+=1
    if to_str:
        rysuj_pascal_triangle(tablica)
    return tablica

def rysuj_pascal_triangle(tablica:list)->None:
    n = len(tablica)
    for entry in enumerate(tablica):
        print(entry[0], end='')
        print(' '*(2*n-entry[0]), end='')
        result = ' '.join(str(item) for item in entry[1])
        print(result, sep=', ',end='\n')


pascal_triangle(7,to_str=True)
