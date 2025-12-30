# Aqui irei criar um programa que ira verificar se tem ou não determinado nome dentro de uma váriavel 

nome = str(input('Digite o seu nome: ')).strip() # com o .strip nós estamos quebrando os espaços antes e depois dos dados da string 

print('Seu nome tem Cristo? {}'.format('cristo' in nome.lower())) # Boa noticia, também podemos usar o .upper ou .lower dentro da linha de print, assim economizando código 


