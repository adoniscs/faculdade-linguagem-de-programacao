ano_inicio = int(input())
ano_fim = int(input())
cont = 0

for ano in range(ano_inicio, ano_fim + 1):
    if ano_fim > 9999:
        break
    elif (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        cont += 1
        print(f'{ano}')
print(f'bissextos: {cont}')
