# Aqui aprenderemos como colocar cores em Python 

#Sempre que quiser representar uma cor em python comeca com o contrabarra \

# O 033 é uma das formas de informar o pc que queremos alterar as cores

# O código é utilizado da seguinte forma, \033[0;33;44m a 1numeração 0 é style da letra a 2numeração 33 é a cor que queremos, a 3numeração 44 é o background, o m é utilizado para finalizar a função de coloração 

# Utilizando no código 

print('\033[4;36;41mOlá mundo ddddddddddddddddddddd!')

# Para cortar a extensão do style temos que encerrar no próprio código exemplo:

print('\033[4;36;41mOlá mundo!\033[m ddddddddddddddddddddd\033[m')


a = 4
b = 5

print('Os valores são \033[4;31m{}\033[m e \033[1;35;40m{}\033[m!!!!'.format(a, b))

# Também podemos resetar isso direto dentro do format, que fica muito mais organizado 

nome = 'Emerson'

print('Olá! Muito prazer em ter conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Podemos fazer também com uma lista já estilizada, para somente pegar as cores e selicionalas 

nome = 'Joicy'
cores = {'limpa':'\033[m'
        , 'Azul':'\033[34m'
        , 'Amarelo':'\033[33m'
        , 'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em conhecer, {} {} {} {} você é linda!!'.format(cores['Azul'], nome, cores['limpa'] ,cores['Azul']))