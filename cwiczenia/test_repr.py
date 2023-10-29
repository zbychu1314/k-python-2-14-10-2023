class Samochod:
    opony = 4
    def __init__(self,marka,kolor):
        self.marka = marka
        self.kolor = kolor
    def __repr__(self):
        return (f'Samochod {self.marka} kolor {self.kolor}')
    def pomaluj(self,kolor):
        self.kolor=kolor
        print(f'Samochod pomalowany na kolor {self.kolor}')

class Ford(Samochod):
    def pomaluj(self, kolor):
        super().pomaluj(kolor)
        print('Ford ma czarny dach')

s1 = Samochod('Opel','Czerwony')
s1.pomaluj('Bialy')

f1 = Ford('Ford','Zielnoy')
f1.pomaluj('Pomaranczowy')

print(hasattr(Samochod,'opony'))
setattr(Samochod,'opony',5)
print(getattr(Samochod,'opony'))
######## any all

def waliduj_liczbe(liczby:list):
    return any((liczba >0) and (liczba%2==0) for liczba in liczby)

liczba = waliduj_liczbe([2,3,4,51])
#print(liczba)

def generator():
    yield 1
    yield 2
    yield 3

print(generator().__next__())
print(generator().__next__())