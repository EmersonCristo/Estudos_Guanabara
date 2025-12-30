# Desafio que tem que dar um valor verdadeiro a cidade de nascimento 

cidade = str(input('Digite a cidade em que você nasceu: '))

print(cidade.lower().find('são'))

# Forma que o professor fez 

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].lower() == 'santo') # nessa linha estou pegando os 5 primeiros caracteres e perguntando ao sistema se ele é igual a santo