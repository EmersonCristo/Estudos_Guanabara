# Utilizando o mesmo exemplo do código da aula passada 

sal = float(input('Digite o salário do funcionario: '))

novo = sal + (sal * 15 / 100)

print('O sálario do funcionario Emerson que era {:.3f}R$, agora passa a ser {:.3f}' .format(sal, novo))