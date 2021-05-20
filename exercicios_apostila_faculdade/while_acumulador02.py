credito = float(input('Seu crédito: ')) # variavel acumuladora
total = 0 # variavel acumuladora
preco = float(input('Preco do item: '))

while credito >= preco:
    total += preco
    credito -= preco
    preco = float(input('Preco do item: '))

print(f'total da compra: R$ {total:.2f}')
print(f'crédito restante: R$ {credito:.2f}')
