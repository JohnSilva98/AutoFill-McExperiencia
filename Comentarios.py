from faker import Faker
import random

fake = Faker()

positive_comments = [
    "Adorei o lugar, a comida é incrível!",
    "O atendimento foi excelente e o lanche estava delicioso!",
    "Eu definitivamente gosto e recomendo!",
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
    "McDonald's como sempre muito bom"
    "O atendimento foi super ágil e os funcionários foram mega simpáticos."
    "O hambúrguer tava top, um dos melhores que já comi."
    "Quem dera todo lugar fosse assim, atendimento rápido e lanche gostoso demais."
    "Os molhos daqui são os melhores, combinavam demais com o lanche.!"
    "Os ingredientes eram fresquinhos e bem escolhidos, isso faz toda a diferença."
    "O atendimento foi tão bom que me senti em casa, os caras são muito gente boa."
    "A carne do hambúrguer tava no ponto certo, mal posso esperar pra comer de novo."
    "Atendimento rápido e lanche de qualidade, assim é que é bom!"
    "Tava com muita fome e o lanche msalvou, fiquei bem satisfeito."  
    "Tava com receio de pedir algo diferente, mas me surpreendi, o lanche era bom demais."
    "O pessoal que trabalha lá é muito prestativo, o que é raro de se encontrar hoje em dia."
    "Comida boa, atendimento bom e preço justo"
    "O atendimento foi super rápido, já virou meu lugar preferido"
    "O atendimento foi top, pessoal bem animado e simpático!"
    "Esse lanche estava uma delícia, nota 10 "
    "Atendimento ágil e simpático"

]
#variavel que recebe o comentario aleatorio
comment = random.choice(positive_comments)

