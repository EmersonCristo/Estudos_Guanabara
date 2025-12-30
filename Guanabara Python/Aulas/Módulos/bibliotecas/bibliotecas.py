# Importando bibliotecas 
# As bibliotecas são algo que facilita muito um código, elas meio que fazem as partes do código, no caso acima é uma bibliotca de matematica 

import math 

num = int(input('Digite um número: '))
raiz = math.sqrt(num) # raiz vai receber a raiz da variavel num 

print('A raiz quadrada de {:.1f} é {:.1f}' .format(num, math.ceil(raiz))) #com esses comando estamos pedindo para arredondar o valor para cima 

# IMPORTANDO ITENS, PORÉM, DE FORMA EXCLUSIVA 

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num) #aqui podemos ver que puxando itens especificos da biblioteca, nós não precisamos usar o math.sqrt somente o sqrt

print('A raiz de {} é igual a {:.2f}' .format(num, floor(raiz))) # O mesmo exemplo do comentário acima 

# Outros exemplos de bibliotecas 

# Biblioteca que gera números aleatórios 
import random

num = random.randint(1, 10) #Aqui estamos determinando que os números tem que ser de 1 até 10

print(num)

# Para instalar uma biblioteca que não vem como padrão em python, tem diferentes maneiras dependendo da ferramenta, como eu estou utilizando o VSCODE eu abro o terminal e instalo ela lá, ai depende real de que ferramenta estamos utilizando no momento. Existem bibliotecas criadas por outras pessoas como provavelmente essa utilizada abaixo 

import emoji

print(emoji.emojize('Olá, você está aprendendo Python :earth_americas:', use_aliases=True)) # precisamos de tudo isso para utilizar uma biblioteca importada 









