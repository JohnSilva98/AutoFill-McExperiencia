from faker import Faker
import random
import re


fake = Faker('pt_BR')
people_list = []

# adicionando 3 pessoas à lista
for i in range(3):
    first_name = fake.first_name()
    last_name = fake.last_name()
    fullname = re.sub(r"\s+", "-", first_name + " " + last_name)
    telefone = fake.phone_number(area_code='11')
    email= fullname.lower() + "@gmail.com"
    person = {"nome": first_name, "sobrenome": last_name, "telefone": telefone, "email":email}
    people_list.append(person)

#variavel que recebe a pessoa gerada
pessoa=random.choice(people_list)



