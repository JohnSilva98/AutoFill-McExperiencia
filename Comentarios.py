from faker import Faker
import random

fake = Faker()

positive_comments = [
    "Adorei o lugar, a comida é incrível!",
    "O atendimento foi excelente e o lanche estava delicioso!",
    "Eu definitivamente gosto e  recomendo!",
    "Sem dúvida, este é um dos melhores McDonald's que já fui. A comida é incrível e o ambiente é limpo!"
    "O atendimento foi rápido, os atendentes super atenciosos"
    "Lanche gostoso, muito bom nota 10"
    "atendimento rápido, lanche mto bom"
    "restaurante limpo, funcionários simpáticos, comida boa"
    "tudo top"
    "top"
    "top demais, pessoal atencioso"
    "todos são atenciosos, principalmente com as crianças, meu filho amou"
    "Local limpo e agradavel, o lanche veio perfeito e quentinho"
    "Gostei do lugar, o lanche veio rapidinho, tudo certo"
    "top dms, mto bom"
    


]
#variavel que recebe o comentario aleatorio
comment = random.choice(positive_comments)

