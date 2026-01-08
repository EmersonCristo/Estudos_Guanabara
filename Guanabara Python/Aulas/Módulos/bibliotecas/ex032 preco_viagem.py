# DESAFIO Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. 

distancia = int(input('Digite as distancia percorrida na viagem: '))

if (distancia < 200):
    d = 0.50
    print('A distância percorrida é de {}km, e o valor é {:.2f}R$'.format(distancia, (distancia * d)))

else:
    d = 0.45
    print('Como a viagem é mais de 200km, o valor por km é menor a viagem está no valor de {:.2f}R$'.format(distancia * d))

# TAMBÉM PODEMOS FAZER TODO ESSE CÓDIGO NA MESMA LINHA 

# preco = distancia * 0.50 if distancia <=200 else distancia *0.45 
# Na linha de cima podemos simplificar todo o código de cima, porém, essa tecnica não parece ser muito utilizada no mercado 


