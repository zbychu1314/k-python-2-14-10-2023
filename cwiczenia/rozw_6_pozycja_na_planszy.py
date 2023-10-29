def okresl_pozycje(x:int,y:int)->str:
    if x and y in range(0,101):
            x = int(x)
            y = int(y)
            if x and y in range (0,10):
                return 'Lewy Dolny Róg'
            elif x in range (0,10) and y in range (10,90):
                return 'Lewa Krawedź'
            elif x in range (0,10) and y in range (90,101):
                return 'Lewa Górny Róg'
            elif x in range (10,90) and y in range (0,10):
                return 'Dolna Krawedź'
            elif x in range (10,90) and y in range (10,90):
                return 'Centrum'
            elif x in range (10,90) and y in range (90,101):
                return 'Górna Krawedź'
            elif x in range (90,100) and y in range (0,10):
                return 'Prawy Dolny Róg'
            elif x in range (90,100) and y in range (10,90):
                return 'Prawa Krawędź'
            elif x in range (90,100) and y in range (90,101):
                return 'Prawy Górny Róg'
    else:
        print('Wprowadzono niepoprawne dane')
print(okresl_pozycje(9,9))
print(okresl_pozycje(9,20))
print(okresl_pozycje(9,100))
print(okresl_pozycje(20,0))
print(okresl_pozycje(20,20))
print(okresl_pozycje(20,100))
print(okresl_pozycje(90,0))
print(okresl_pozycje(90,20))
print(okresl_pozycje(90,100))
        