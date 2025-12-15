larg = float(input('Digite a Largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.1f}m2 ' .format(larg, alt, área))

tinta = área / 2 #a cada 2 metros se gasta 1 litro de tinta 

print('Para pintar essa parede, você precisará de {}l de tinta.' .format(tinta))
