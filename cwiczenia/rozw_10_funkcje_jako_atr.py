liczby = [ 2, 3, 5, 10, 46, 73, 90]
def start(liczby):
    for i, liczba in enumerate(liczby):
        if liczba >=5:
            return i
def stop(liczby):
    for i, liczba in enumerate(liczby):
        if liczba >70:
            return i
def wytnij(liczby,*,start,stop):
    start_index=start(liczby)
    stop_index=stop(liczby)
    print(liczby[start_index:stop_index])

wytnij(liczby,start=start,stop=stop)