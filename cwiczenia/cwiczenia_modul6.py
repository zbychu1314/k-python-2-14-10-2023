x=5
x = 'X wieksze niz 10' if x >10 else 'X mniejsze niz 10' 
print(x)

################################################################

liczby = [1,2,3,4,5]

zmodyfikowane_liczby = [x**2 if x%2==0 else -1 for x in liczby ]
print(zmodyfikowane_liczby)


parzyste_kwadraty ={x:x**2 if x%2==0 else -1 for x in liczby}
print(parzyste_kwadraty)