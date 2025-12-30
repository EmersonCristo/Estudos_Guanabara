# QUEBRANDO UM NÚMERO REAL 

import math

num = float(input('Digite um valor: '))
print("O valor digitado é {} e a sua porção inteira é {}" .format(num, math.trunc(num))) #trunc vai cortar o número digitado apenas para o seu valor inteiro 

# A outra forma só que com exclusividade, esse é o modelo ideal, pois deixa o código "Mais leve"

from math import trunc

num = float(input('Digite um valor: '))
print("O valor digitado é {} e a sua porção inteira é {}" .format(num, trunc(num))) 

# Também temos outro modelo que pode ser utilizado, que é o seguinte modelo:

num = float(input('Digite um valor: '))
print('O valor digitado é {} e a sua porção inteira é {}' .format(num, int(num)))