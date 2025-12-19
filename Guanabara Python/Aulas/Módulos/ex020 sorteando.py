# Fazendo um sistema para sortear os alunos 

import random

nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite outro nome: ')
nome4 = input('Digite outro nome: ')

lista = [nome1, nome2, nome3, nome4]

escolhido = random.choice(lista) #Uma escolha dentro da lista

print('O aluno escolhido foi {}' .format(escolhido))

# Exclusividade 

from random import choice

nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite outro nome: ')
nome4 = input('Digite outro nome: ')

lista = [nome1, nome2, nome3, nome4]

escolhido = choice(lista) #Uma escolha dentro da lista

print('O aluno escolhido foi {}' .format(escolhido))