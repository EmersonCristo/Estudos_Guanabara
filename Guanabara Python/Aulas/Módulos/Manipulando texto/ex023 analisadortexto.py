# Desenvolvendo um sistema que analisa o texto que escrevemos, com base no que aprendi na aula passada 

nome = str(input('Digite seu nome: ')).strip()    # Aprendizado novo, podemos já incluir o strip para anular os espaços de uma variavel, assim podemos contar os caracteres de forma correta 

print('Seu nome em maiúsculas é {}' .format(nome.upper()))

print('Seu nome em minúsculas é {}' .format(nome.lower()))

print('Seu nome tem um total de {} de letras' .format(len(nome)- nome.count(' '))) # O strip vai tirar todos os espaços em volta da string menos o que está dentro dela, ai adicionamos esse nome.count('espaço') que ele vai contar quantos espaços tem e contabilizar essa quantidade de forma negativa

print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # Aqui para achar o primeiro nome contaremos até quando chegar no primeiro espaço, o (SEPARADOR), assim acharemos onde termina o primeiro dado digitado pelo usuário

# Támbem podemos fazer a função acima da devida maneira 

separa = nome.split() 

print('Seu primeiro nome é {} e ele tem {} letras ' .format(separa[0], len(separa[0])))