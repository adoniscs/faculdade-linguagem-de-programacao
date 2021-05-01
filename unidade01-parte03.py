# criar um programa para um site! O programa deverá
# solicitar o valor de um item e a quantidade de
# unidades compradas deste item, ao final deve exibir
# o tatal com desconto de 10%. Considere que a 
# quantidade será um número natural positivo.

valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Quantidade: '))
valor_total = valor_produto * qtd_produto
desconto = 0.10
desconto_produto = valor_total * desconto
preco_total_produto = valor_total - desconto_produto
print(f'O valor total da compra foi de R${valor_total:.2f}')
print(f'Você teve um desconto de R${desconto_produto:.2f}')
print(f'O valor total a ser pago é de R${preco_total_produto:.2f}')