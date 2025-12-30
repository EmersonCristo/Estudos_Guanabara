# Estudos a seguir é sobre o controle dos textos em Python

frase = 'Curso em Vídeo'

print(frase)
print(frase[3:13]) # Do 3 a 13
print(frase[:13]) # Como não tem nada indicando por onde começar, ele vai no inicio mesmo 
print(frase[13:]) # Do 13 a todos
print(frase[1:15]) # Começa pela primera letra que no caso é u e vai até o caractére de número 15
print(frase[1:15:2]) # O ultimo número no caso o 2, refere a de quantos em quantos números nós iremos, no caso pulando de 2 em 2
print(frase[1::2]) # Do 1 a todos, pulando de 2 em 2 
print(frase[::2]) # Pulando de 2 em 2 


# BUSCA NO POR LETRAS E ALTERAÇÃO DAS MESMAS 

frase = 'Curso em Vídeo'

print(frase.count('o')) # Quantas vezes o o aparece na variavel
print(frase.count('o')) # Importante lembrar que o "o" diferencia do "O" 
print(frase.upper().count('0')) # Aqui estamos pedindo para converter toda a strinf em maiuscula, e depois pedindo pelas letras O em maisculo, que vão aparecer todas pois acabaram de ser convertidas em O maiusculo 


# CONTANDO A QUANTIDADE DE CARACTERES NA VARIAVEL 

print(len(frase)) # Aqui estamos pedindo para contar o tamanho da variavel, o tanto de caracteres que a mesma possui 


# REMOVENDO ESPAÇOS ANTES E DEPOIS OU SOMENTE ANTES OU SOMENTE DEPOIS DE DETERMINADA FRASE

print(len(frase.strip())) # Aqui estamos pedindo para ler a tamanho da frase, e o .strip é para anular qualquer espaço desnecessario que estaja em torno da variavel 
print(len(frase.rstrip())) # Aqui estamos pedindo para remover A ESQUERDA o Right que estiver sobrando espaços da variavel
print(len(frase.lstrip())) # Aqui estamos pedindo para remover apenas A DIREITA que estiver sobrando espaços da variavel


# ALTERANDO OS DADOS ||| IMPORTANTE LEMBRAR QUE A FRASE EM SI, A VARIAVEL EM SI, NUNCA MUDA 

frase = 'Curso em Vídeo Python' 

print(frase.replace('Python', 'Android')) # A frase da string somente é apresentada diferente se usarmos o print no proprio código caso contrario NADA altera a variavel 
print(frase) # Só para mostrar que a variavel não foi alterada 

# Agora podemos alterar se fizermos esse processo a seguir:

# frase = print(frase.replace('Python', 'Android')) AQUI SIM ALTERAMOS A FRASE 


# TAMBEM PODEMOS PERGUNTAR SE DETERMINADA FRASE SE ENCONTRA DENTRO DA VARIAVEL 

frase = "Curso em Video Python"

print('Curso' in frase) # Curso está na variavel frase? Resposta = True,, e quando não, False 
print(frase.lower().find('video')) # Aqui o código vai informar a partir de qual caractere na string vai começar a palavra que estamos procurando. Antes de tudo é bom verificar que primeiro para dar certo a busca, nós deixamos todos os caracteres da variavel em minuscula com o frase.lower



# TAMBEM PODEMOS DIVIDIR A VARIAVEL, ASSIM TRANSFORMANDO ELA EM UMA LISTA 

frase = 'Curso em Video Python'

print(frase.split()) # Vai transformar em uma lista com os 4 itens
dividido = frase.split() # Aqui nos formamos outra variavel(lista) com os dados da variavel frase 
print(dividido[0]) # Printar dividido no indice 0, que é pra ser o Curso
print(dividido[2][3]) # Pegue o dividido no indice 2(Video), e me mostre o indice 3, que em video é o E



# DICA ALEATORIA DO GUANABARA 

# Se a pessoa quiser pegar um texto que está no código python e transforma-lo em um print para o usuário poder lê, basta colocar o print com (3) aspas (""") e finalizando com 3 aspas duplas também (""")
