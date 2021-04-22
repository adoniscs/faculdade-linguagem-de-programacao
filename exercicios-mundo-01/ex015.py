"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km percorridos? '))
valor_alugado = dias_alugado * 60
valor_km = km_rodados * 0.15
total_pagar = valor_alugado + valor_km
print('O valor pela quantidade de dias é de R${}, o valor a ser cobrado pela kilometragem rodada será de R${}.\n'
      'O valor total a ser pago será de R${}'.format(valor_alugado, valor_km, total_pagar))