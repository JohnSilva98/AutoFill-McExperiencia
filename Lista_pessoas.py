from faker import Faker
import random

fake = Faker('pt_BR')
people_list = []

# adicionando 500 pessoas à lista
for i in range(500):
    first_name = fake.first_name()
    last_name = fake.last_name()
    person = {"nome": first_name, "sobrenome": last_name, "telefone": fake.phone_number(), "email": f"{first_name.lower()}.{last_name.lower()}@gmail.com"}
    people_list.append(person)

# imprimindo as informações de uma pessoa aleatória da lista
print(random.choice(people_list))
