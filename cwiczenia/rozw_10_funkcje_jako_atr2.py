znaki="12312456078"
def start(liczby):
    for i, liczba in enumerate(znaki):
        if liczba == str(3):
            return i
def stop(liczby):
    for i, liczba in enumerate(znaki):
        if liczba == str(7):
            return i
def wytnij(znaki,*,start,stop):
    start_index=start(znaki)
    stop_index=stop(znaki)
    print(znaki[start_index:stop_index+1])

wytnij(znaki,start=start,stop=stop)