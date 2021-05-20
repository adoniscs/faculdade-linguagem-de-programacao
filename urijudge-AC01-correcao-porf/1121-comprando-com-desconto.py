preco = float(input())
qtd = int(input())

total = preco * qtd
desconto = (total * (10 + qtd)) / 100
final = total - desconto

print(f'{total:.2f}')
print(f'{final:.2f}')
