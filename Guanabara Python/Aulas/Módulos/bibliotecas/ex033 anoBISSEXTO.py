# Aqui iremos analisar se o ano é bissexto, ano bissexto é um ano que é acrecentado um dia a mais em fevereiro assim o ano tem 366 dias

from datetime import date #biblioteca de data, para puxar a data ou hora atual etc

ano = int(input('Digite o ano que você deseja analisar? Coloque 0  para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year #Aqui estamos pegando a data de hoje, porém, somente o ano 

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #resto da divisão por 4 é 0 E resto da divisão por 100 é diferente de 0 OU resto da divisão por 400 é 0 
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))