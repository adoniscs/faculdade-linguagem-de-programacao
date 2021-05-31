i = 0
v = 5 * [0]

while i < 5:
    v[i] = int(input('Digite um valor: '))
    i += 1

print('\nValores Digitados: ')

i = 0
while i < 5:
    print('Valor no índice ', i, ' = ', v[i])
    i += 1