# Calculando de forma normal sem biblioteca 

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do catato adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2) # 1/2 significa meio 

print('A hipotenusa vai medir {:.2f}' .format(hi))

# Fazendo a mesma coisa, porém, com biblioteca 

import math 

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do catato adjacente: '))
hi = math.hypot(co, ca) #hypot é calculo da hipotenusa dentro da biblioteca math (matematica)

print('A hipotenusa vai medir {:.2f}' .format(hi))

# Importando somente a hipotenusa da biblioteca

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do catato adjacente: '))
hi = hypot(co, ca) #hypot é calculo da hipotenusa dentro da biblioteca math (matematica)