"""
crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos Dólares ela pode comprar. Considere: US$1,00 = 5,57
"""
dinheiro = float(input('Digite a quantia que você tem R$'))
conversao = dinheiro / 5.57
print(f'Com essse valor em dinheiro, você pode comprar US${conversao:.2f}')
