from decimal import Decimal

###lepiej korzystac z decimala 

print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')==Decimal('0.3'))

print(round(0.1 + 0.1 + 0.1,2) == round(0.3,2))

