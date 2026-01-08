# Guanabara propos um desafio de fazer um programa que o usuario tenta adivinhar um número que o computador escolher de 0 a 5

from random import randint
from time import sleep #biblioteca MUITO bacana em python, ira dar a entender que o computador está pensando, para o nosso jogo isso é ótimo 

computador = randint(0,5) # faz o computador pensar em um número de 0 a 5

print('-=-'*20)
print('Estou pensando em um número, tenta adivinhar')
print('-=-'*20)

num = int(input('Digite um número de 0 a 5: ')) # para o jogador tentar adivinhar o número 

print('PROCESSANDO.......')
sleep(2)

if (num == computador):
    print('Parabens! Você conseguiu acerta o número em que eu estava pensando.')

else:
    print('Ganhei! Eu pensei no número {}, e você digitou o número {}'.format(computador, num))

print('-=-'*20)

    #Consegui