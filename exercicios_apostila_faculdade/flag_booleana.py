total = 0
quero_comprar = True # será usada como flag booleana

while quero_comprar:
    preco = float(input('Preço: '))
    total += preco
    opcao = input('Continuar comprando (s/n)? ')

    if opcao != 's':
        quero_comprar = False

print(f'Total da compra: R$ {total:.2f}')
