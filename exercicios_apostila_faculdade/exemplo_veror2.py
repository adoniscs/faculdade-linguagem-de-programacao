i = 0
v1 = []

while i < 5:
    v1.append(int(input('Digite um valor: ')))
    i += 1

print('\nValores digitados: ')

i = 0

while i < 5:
    print(f'Valor no índice {i} = {v1[i]}')
    i += 1