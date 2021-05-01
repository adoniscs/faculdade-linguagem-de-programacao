dia = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
diaDaCompra = input('Informe o dia da semana: ')
diasParaEntrega = int(input('Informe a quantidade de dias: '))

if diasParaEntrega >= 0 and diasParaEntrega <= 6:

    if diasParaEntrega == 0:

        print('chega hoje!')
    else:
        for x in range(dia.__len__()):
            if dia[x] == diaDaCompra:
                diaAtual = x

        while diasParaEntrega > 0:
            diaAtual = diaAtual + 1
            diasParaEntrega = diasParaEntrega - 1
            if diaAtual == 7:
                diaAtual = 0
        print(f'sera entregue {dia[diaAtual]}')
