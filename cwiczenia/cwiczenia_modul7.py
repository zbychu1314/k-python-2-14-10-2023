temperatura = 1

match temperatura:
    case 11:
        print('Temperatura 11')
    case 0:
        print('Temperatura 0')
    case 1 | 2:
        print('takie tam')
    case _:
        print('pozostale')


punkt = (1, 1)

match punkt:
    case (0, 0):
        print("Początek układu współrzędnych")
    case (x, 0):
        print(f"Punkt ({x}, 0) leży na osi X")
    case (0, y):
        print(f"Punkt (0, {y}) leży na osi Y")
    case (x, y):
        print(f"Punkt ({x}, {y}) leży w przestrzeni 2D")
    case _:
        print("Nieznany typ danych")

##############################################

dane ={"wiek": 25, "wzrost": 180}

match dane:
    case {"wiek": n, "wzrost": y} if n < 18 and y > 150:
        print(f"Mniej niż 18 lat a wysoki ({y})")
    case {"wiek": n, "waga": z} if n >= 18:
        print("18 lat lub więcej")
    case {"wiek": n, "wzrost": z} if n >= 18:
        print("18 lat lub więcej + wzrost nieznany")
    case _:
        print("Nie można określić wieku")

################################################

shape = {'type':'square','side':10}
shape = {'type':'circle','radius':2}

match shape:
    case {'type':'square','side':s}:
        print(f'Pole kwadratu wynosi {s**2}')
    case {'type':'circle','radius':s}:
        print(f'Pole koła wynosi {s**2}')

######################################################
if shape['type'] =='square':
    print(f'Pole kwadratu wynosi {s**2}')
if shape['type'] =='circle':
    print(f'Pole koła wynosi {s**2}')


##########################

