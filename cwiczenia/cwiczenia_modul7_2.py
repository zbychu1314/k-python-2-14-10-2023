from faker import Faker 

fake = Faker("pl_PL")
name = fake.name()
address = fake.address()
text = fake.text(50)
print(name)
print(address)
print(text)