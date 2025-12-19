# Confesso que sobre seno cosseno e tangente eu preciso estudar mais, porém, aqui está como é feito o seu calculo utilizando python 

import math 

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radius(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(ângulo, seno))
cosseno = math.cos(math.radius(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(ângulo, cosseno))
tangente = math.tan(math.radius(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(ângulo, tangente))

# Novamente mostrando o código com apenas as ferramentas que utilizamos no código 

from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(ângulo, tangente))
