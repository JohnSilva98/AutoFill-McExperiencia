from faker import Faker
import random

fake = Faker('pt_BR')
people_list = []

# adicionando 3 pessoas à lista
for i in range(3):
    first_name = fake.first_name()
    last_name = fake.last_name().replace(" ", "")
    telefone = fake.phone_number()
    email= f"{first_name.lower()}.{last_name.lower()}@gmail.com"
    person = {"nome": first_name, "sobrenome": last_name, "telefone": telefone, "email":email}
    people_list.append(person)

#variavel que recebe a pessoa gerada
pessoa=random.choice(people_list)



