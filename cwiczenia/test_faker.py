from faker import Faker


typy = ['samochód','rower','motocykl']
marka_samochod = ['Toyota','Ford','Opel','Tesla']
marka_rower = ['Korss','Scott','KTM','Ghost']
marka_motocykl = ['Honda','Kawasaki','BMW','Suzuki']
model_samochod = ['model_samochod']
model_rower = ['model_rower']
model_motocykl = ['model_motocykl']

YEAR_INIT = 1900
YEAR_END = 2023

def generuj_dane(number:int):
    index =0    
    while index < number:
        item_atrr =[]
        item = fake.random.choice(typy)
        item_atrr.append(item)
        year = fake.random.randint(YEAR_INIT,YEAR_END)
        item_atrr.append(year)
        if 'samochód' in item:
            item = fake.random.choice(marka_samochod)
            item_atrr.append(item)
            item = fake.random.choice(model_samochod)
            item_atrr.append(item)
        if 'rower' in item:
            item = fake.name()
            item_atrr.append(item)
            item = fake.word()
            item_atrr.append(item)
        if 'motocykl' in item:
            item = fake.random.choice(marka_motocykl)
            item_atrr.append(item)
            item = fake.random.choice(model_motocykl)
            item_atrr.append(item)
        print(item_atrr)
        index=index+1

fake = Faker()
generuj_dane(20)