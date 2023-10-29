import random

N = 20

liczby = [random.randint(1,200) for _ in range(0,N)]
liczby.sort()
print(liczby)

def if_greater_than_5(number):
    if number >5:
        return True

def if_greater_than_70(number):
    if number >70:
        return True

def wytnij(liczby,start=if_greater_than_5,stop=if_greater_than_70):
    wytnij.start = []
    wytnij.stop = []
    start = 0
    stop = 0
    for liczba in liczby:
        wytnij.start.append(if_greater_than_5(liczba))
        wytnij.stop.append(if_greater_than_70(liczba))
    for i,start_item in enumerate(wytnij.start):
        if start_item:
            start=liczby.index(liczby[i])
            print(start)
            break
        continue
    for i,stop_item in enumerate(wytnij.stop):
        if stop_item:
            stop=liczby.index(liczby[i])
            print(stop)
            break
        continue
    print(liczby[start:stop])

        
wytnij(liczby)