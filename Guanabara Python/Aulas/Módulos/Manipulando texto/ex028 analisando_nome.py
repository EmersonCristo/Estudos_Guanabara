# Desafio fazendo sozinho 

nome = str(input('Digite seu nome completo:')).strip().upper()
n = nome.split() # Quebrando a variavel nome em uma lista 

print('Muito prazer em conhecer você!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(nome)-1])) #Para pegar a última posição, o -1 pega os números da lista vindo pela contra mão kkkjj 
