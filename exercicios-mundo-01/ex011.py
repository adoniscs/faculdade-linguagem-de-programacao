"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua
área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta,
pinta uma área de 2m².
"""
largura_parede = float(input('Digite a largura da parede: '))
altura_parede = float(input('Digite a altura da parede: '))
area_parede = largura_parede * altura_parede
qtd_tinta = area_parede / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, será necessário {}L de tinta.'
      .format(largura_parede, altura_parede, area_parede, qtd_tinta))
