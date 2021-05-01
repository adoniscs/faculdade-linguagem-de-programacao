preco_prod = float(input())
qtd_prod = int(input())

preco_compra = preco_prod * qtd_prod
desc = preco_compra * 0.1 + (qtd_prod * 0.01) * preco_compra
preco_desc = preco_compra - desc

print(f'{preco_compra:.2f}')
print(f'{preco_desc:.2f}')
