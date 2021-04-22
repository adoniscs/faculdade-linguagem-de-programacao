# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros
medida = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, (medida * 100), (medida * 1000)))
