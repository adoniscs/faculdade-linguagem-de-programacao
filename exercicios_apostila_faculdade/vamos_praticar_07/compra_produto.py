credito = float(input('Seu crédito: '))
total = 0
qtd_item = 1
preco = float(input(f'Preco do item {qtd_item}: '))

while credito >= preco:
    qtd_item += 1
    total += preco
    credito -= preco
    preco = float(input(f'Preco do item {qtd_item}: '))
    
    if preco > credito:
        qtd_item -= 1
        print(f'Compra do item {qtd_item} negada!')

print(f'Items comprados: {qtd_item}')
print(f'O total da compra é de R$ {total:.2f}')
print(f'Crédito restante é de R$ {credito:.2f}')
