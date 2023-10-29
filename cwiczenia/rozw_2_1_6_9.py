def filtruj_wiadomosci(wiadomosc:str)->bool:
    if ('PROMOCJA' in wiadomosc or len(wiadomosc) <5 or '!!!' in wiadomosc):
        return False
    else:
        return True
print(filtruj_wiadomosci('PROMOCJA'))
assert filtruj_wiadomosci('PROMOCJA') is False
assert filtruj_wiadomosci('222') is False
assert filtruj_wiadomosci('!!!') is False
assert filtruj_wiadomosci('MOJASSS') is True
#print(filtruj_wiadomosci('3333333333333'))