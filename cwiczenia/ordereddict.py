from collections import OrderedDict

def type_items(quantity:int)->OrderedDict:
    ordered_dict = OrderedDict()
    for item in range(0,quantity):
        input_text = input().split(' ')
        for i in input_text:
            index=0
            if not i.isalpha():
                price = int(i)
                index = input_text.index(i)
            product = ' '.join(str(e) for e in input_text[0:index])
        if product in ordered_dict.keys():
            value = ordered_dict[product]
            ordered_dict[product] = int(value)+int(price)
        else:
            ordered_dict[product]=int(price)
    for key, val in ordered_dict.items():
        print(key,val) 

#ordered_dictionary = OrderedDict()
#ordered_dictionary['a'] = 1
#ordered_dictionary['b'] = 2
#ordered_dictionary['c'] = 3
#ordered_dictionary['d'] = 4
#ordered_dictionary['e'] = 5
number_products = input()
type_items(int(number_products))
