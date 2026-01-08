# Exercicio de radar, caso o carro passe a mais de 80 será multado, multa vai de acordo com a velocidade a cada 1km/h acima da velocidade a multa aumenta 7 reais 

velocidade = float(input('Qual a velocidade atual do carro? '))

print('='*30)

if (velocidade > 80):
    print('Você está acima do limite de velocidade, MULTADO!')
    multa = (velocidade - 80) * 7
    print('Valor da multa é de {:.2f}R$'.format(multa))

else:
    print('Dentro de limite de velocidade, você é um excelente motorista.')


print('Tenha um bom dia! Dirija com segurança!')

print('='*30)