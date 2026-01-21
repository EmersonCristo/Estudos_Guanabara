a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# if a<b and a<c:
#     menor = a
# if b<c and b<a:
#     menor = b
# if c<a and c<b:
#     menor = c

#Outra forma de fazer o código, porém, de forma mais simples 

# Aqui iremos começar o código já descartando o primeiro if, iremos começar o programa considerando o a menor de todos 

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#No exemplo acima o a já vem como menor, porém, se b ou c for menor, eles tomam a variavel menor para si 

# Da mesma forma, iremos analisar que é o maior valor digitado 

maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Irei fazer o valor médio 

medio = a
if b < a and b > c or b > a and b < c:
    medio = b
if c < a and c > b or c > a and c < b:
    medio = c


print('O menor valor digitado foi o valor {}'.format(menor))
print('O valor medio digitado foi o valor {}'.format(medio))
print('O maior valor digitado foi o valor {}'.format(maior))