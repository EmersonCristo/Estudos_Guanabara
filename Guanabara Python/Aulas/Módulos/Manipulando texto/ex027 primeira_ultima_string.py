frase = str(input('Digite uma frase: ')).upper().strip() #Podemos adicionar mais de uma ferramenta por linha 

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1)) # Aqui a unica coisa fora do normal, é que estamos adicionando o número + 1 para ficar similar a nossa contagem humana, pois, para a máquina a contagem começa com o 0 
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1)) # Aqui colocamos o rfind, para ele começar a procurar da direita para a esquerda  

# O USUARIO É A PIOR RAÇA QUE TEM byGustavo Guanabara 

