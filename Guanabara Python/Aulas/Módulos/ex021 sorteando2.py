import random

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista) #Aqui estamos mandando o código embaralhar a lista

print(lista)

# Agora estou fazendo sozinho o sistema com base no que sei que o professor vai pedir 

from random import shuffle

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4]

shuffle(lista) #Aqui estamos mandando o código embaralhar a lista

print(lista)