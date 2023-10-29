def formatuj(*args,**kwargs):
    napis ="\n".join(args)
    for key, value in kwargs.items():
        napis=napis.replace('$'+key,str(value))
    return napis
    

print(formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10,))


#>>> formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10,)
#'koszt 10 PLN\nkwota 10 brutto'
#
#>>> formatuj('koszt cena PLN', 'kwota $cena brutto', cena=10,)
#'koszt cena PLN\nkwota 10 brutto'
#
#>>> formatuj('kwota $cena brutto', cena=10,)
#'kwota 10 brutto'
#
#>>> formatuj("$a, $A")
#'$a, $A'
#
#>>> formatuj("$a, $A", a=14, A=20)
#'14, 20'
#
#
#>>> formatuj("$a, $A", "B", "$a" a=14, A=20)
#'14, 20\nB\n14'