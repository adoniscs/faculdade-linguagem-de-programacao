"""
faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco_produto = float(input('Qual é o preço do produto? R$'))
desconto_produto = preco_produto - (preco_produto * 5 / 100)
print('O preço do produto com desconto de 5% fica R${:.2f}'.format(desconto_produto))