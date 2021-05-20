total = 0 # variavel acumuladora

preco = float(input('preço do item: '))

while preco != -1:
    total += preco
    preco = float(input('preco do item: '))

print(f'Total da compra: R$ {total:.2f}')
