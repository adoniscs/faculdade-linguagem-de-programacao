"""
desenvolva um programa que pergunte a distancia de uma
viagem em KM. Calcule o preço da passagem, cobrando
R$0,50 por Km para biagem de até 200km e R$0,45 para
viagens mais longas.
"""
distancia = int(input('Digite a distancia da viagem: '))

if distancia > 0 and distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da viagem com {distancia}Km é de R${valor}')
else:
    valor = distancia * 0.45
    print(f'O valor da viagem com {distancia}Km é de R${valor}')