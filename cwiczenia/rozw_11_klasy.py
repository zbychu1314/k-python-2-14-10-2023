class Ksiazka:
    liczba_ksiazek=0
    def __init__(self,tytul,autor,rok_wydania):
        self.tytul=tytul
        self.autor=autor
        self.rok_wydania=rok_wydania
        self._czy_wypozyczona = False
        #Ksiazka.liczba_ksiazek +=1  
        #self.__class__.liczba_ksiazek +=1  ### bardziej uniwersalne  
        self.incr_counter() ##### korzystajac z metody klasowej

    def wypozycz(self):
        if self._czy_wypozyczona:
            print(f'Ksiazka {self.tytul} jest wypozyczona')
            return
        self._czy_wypozyczona = True
    
    def zwroc(self):
        if self._czy_wypozyczona:
            self._czy_wypozyczona=False
            return
        print(f'Ksiazka {self.tytul} jest już w bibliotece')
    
    def info(self):
        print(f'Tytuł: {self.tytul}, Autor: {self.autor}, Rok Wydania: {self.rok_wydania}')

    @classmethod
    def ile_ksiazek(cls):
        print(f'W systemie mamy {cls.liczba_ksiazek}')

    @classmethod
    def tworz_ksiazki(cls,plik):
        lista_ksiazek =[]
        with open(file=plik) as file:
            for line in file:
                dane = line.split(',')
                ksiazka = Ksiazka(dane[0],dane[1],dane[2])
                lista_ksiazek.append(ksiazka)
        return lista_ksiazek

    @classmethod
    def incr_counter(cls):
        cls.liczba_ksiazek += 1

#ksiazka1 = Ksiazka("wiedzmin","Andrzej Sapkowski",1990)
#ksiazka2 = Ksiazka("Hobbit","Tolkien",1990)

lista_ksiazek=Ksiazka.tworz_ksiazki("ksiazki.txt")
for ksiazki in lista_ksiazek:
    ksiazki.info()

lista_ksiazek[0].wypozycz()
print(lista_ksiazek[0]._czy_wypozyczona)

Ksiazka.ile_ksiazek()



