

# Sempre que fomos calcular um desconto em algo, podemos seguir esse padrão 1500*10/100 "10 porcento de 1500", podemos utilizar esse padrão que será de grande ajuda sempre que for preciso 

# Outro exemplo "Preciso calcurar quanto porcento de juros vou pagar de determinado produto Exemplo: 875*15/100 "15 porcento de 875" e vai sair o resultado 131.15"

preço = float(input('Digite o valor do produto: '))

# desc = preço * 5 / 100
# total = preço - desc

#podemos trocar essa versão que eu fiz acima por:

total = preço - (preço * 5 / 100)

print('O valor do produto de {:.2f}, com o desconto sai por {:.2f}.' .format(preço, total))