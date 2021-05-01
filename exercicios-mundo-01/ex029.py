"""
escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por
cada km acima do limite.
"""
velocidade = int(input('Digite a velicidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R${multa}')