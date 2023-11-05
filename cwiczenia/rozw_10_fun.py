import logging

logging.basicConfig(level=logging.INFO,filename='logs.log')
logger = logging.getLogger(__name__)



def dodaj(x,y):
    logger.info(f'Wywoluje funkcje dodaj z parametrami x= {x}, y={y} ')
    return x+y

def odejmij(x,y):
    logger.info(f'Wywoluje funkcje odejmij z parametrami x= {x}, y={y} ')
    return x-y

def pomnoz(x,y):
    logger.info(f'Wywoluje funkcje pomnoz z parametrami x= {x}, y={y} ')
    return x*y

def podziel(x,y):
    logger.info(f'Wywoluje funkcje podziel z parametrami x= {x}, y={y} ')
    if y ==0:
        logger.error('Dzielenie przez zero')
        return
    return x/y

operacje ={'+':dodaj,
           '-':odejmij,
           '*':pomnoz,
           '/':podziel}

def stworz_logger(prefix):
    def wprowadz_dane():
        x = int(input('Podaj wartosc x: '))
        y = int(input('Podaj wartosc y: '))
        operacja = input('Wybierz operacje (+, -, *, /): ')
        try:
            wynik = operacje[operacja]
            print(f"{prefix}: {wynik}")
        except KeyError as e:
            logger.error(f'Niespodziewany blad {e}')  
        
        print(f'Wynik: {operacje[operacja](x,y)}')
    return wprowadz_dane
        
loguj_zdarzenie = stworz_logger("ZDARZENIE")
loguj_zdarzenie()  # wynik: "ZDARZENIE: Użytkownik się zalogował"