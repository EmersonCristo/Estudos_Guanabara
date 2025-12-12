real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.39
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))