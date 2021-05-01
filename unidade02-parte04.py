# crie um programa que receba como entrada o valor de um produto
# e a quantidade comprada. O programa concederá 10% de desconto
# para compras com total maior ou igual à R$100.00
valor_produto = float(input('Digite o valor do produto: R$'))
qtd_comprada = int(input('Digite a quantidade de produtos: '))
valor_total = valor_produto * qtd_comprada
desconto = 0.10
desconto_produto = valor_total * desconto
preco_produto_desconto = valor_total - desconto_produto

if valor_total >= 100:
    print(f'O valor total do produto seria de R$ {valor_total}, mas você teve um desconto de 10% (R${desconto_produto:.2f}).', end='\n')
    print(f'Valor do produto com desconto: R${preco_produto_desconto:.2f}')
else:
    print(f'O valor total é de R${valor_total:.2f}')
print('Obrigado e volte sempre!')
