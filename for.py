tabuada = int(input('Digite um número para exibir a atabuada: '))
print(f'Tabuada do número {tabuada}')
for valor in range(1, 11, 1):
    print(f'{tabuada} x {valor} = {tabuada * valor}')