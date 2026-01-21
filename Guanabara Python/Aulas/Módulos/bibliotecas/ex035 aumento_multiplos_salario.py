
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100) # Leia como 15% de 100%do salário 
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))