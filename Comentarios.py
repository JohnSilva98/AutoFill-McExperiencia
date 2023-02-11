from faker import Faker
import random

fake = Faker()

positive_comments = [
    "Adorei o lugar, a comida é incrível!",
    "O atendimento foi excelente e o lanche estava delicioso!",
    "Eu definitivamente gosto e  recomendo!",
    "Sem dúvida, este é um dos melhores McDonald's que já fui. A comida é incrível e o ambiente é limpo!",
    "O atendimento foi rápido, os atendentes super atenciosos"
    "Lanche gostoso, muito bom nota 10"
    
]

# imprimindo um comentário positivo aleatório
print(random.choice(positive_comments))
