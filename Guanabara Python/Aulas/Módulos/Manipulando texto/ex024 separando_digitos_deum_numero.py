# Aprendendo com Guanabara

# Faça um programa que leia um níúmero de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um valor de 0 a 9999: '))
n = str(num) # n é uma versão de num, só que em string 

print('Analisando o número {}' .format(num))
print('Unidade: {}' .format(n[3]))
print('Dezena {}' .format(n[2]))
print('Centena {}' .format(n[1]))
print('Milhar {}' .format(n[0]))

# Dessa forma vai dar erro por se o usuário não utilizar todos os números 

# Iremos fazer da forma matematica que também NÃO É A CORRETA, porém, é uma forma de fazer o código com os conhecimentos atuais, a forma correta mesmo de fazer o código e com array que até o momento do curso com o Guanabara ainda não estamos fazendo 

num - int(input('Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}' .format(num))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))