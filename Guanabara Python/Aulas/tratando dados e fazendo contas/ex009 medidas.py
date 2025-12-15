medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = mm * 10
dm = cm * 10
dam = medida / 10
hm = medida / 100
km = medida /1000
# print('A medida que você digitou é {:.0f}m medida em cm é {:.0f}, enquanto a medida em mm é {:.0f}' .format(medida, cm, mm))
print('A medida selecionada é {}m \n Em mm {} \n Em cm {} \n Em dm {} \n Em dam {} \n Em hm {} \n Em km {}' .format(medida, mm, cm, dm, dam, hm, km))