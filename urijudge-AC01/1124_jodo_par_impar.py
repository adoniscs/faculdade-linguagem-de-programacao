numero = int(input())

if numero >= 2 and numero % 2 == 0:
    print(f'{numero - 1} {numero + 2}')
else:
    print(f'{numero - 2} {numero + 1}')
