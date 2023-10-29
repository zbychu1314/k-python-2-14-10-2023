dowolny_tekst=b'dowolny tekst'

teskt = 'Przykładowy teścik'
print(teskt)
tekst_zakodowany=teskt.encode("utf-8")
print(tekst_zakodowany)
tekst_odkodowany=tekst_zakodowany.decode()
print(print(tekst_odkodowany))

tekst_zakodowany=teskt.encode("ascii")
print(tekst_zakodowany)
tekst_odkodowany=tekst_zakodowany.decode()
print(print(tekst_odkodowany))

tekst_zakodowany=teskt.encode("utf-16")
print(tekst_zakodowany)
tekst_odkodowany=tekst_zakodowany.decode()
print(print(tekst_odkodowany))



