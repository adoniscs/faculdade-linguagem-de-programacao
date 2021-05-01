diaDaSemana = input()
prazo = int(input())

if prazo == 0:
    print('chega hoje!')

else:
    if diaDaSemana == 'domingo':
        diaEmNumeros = 0

    elif diaDaSemana == 'segunda':
        diaEmNumeros = 1

    elif diaDaSemana == 'terca':
        diaEmNumeros = 2

    elif diaDaSemana == 'quarta':
        diaEmNumeros = 3

    elif diaDaSemana == 'quinta':
        diaEmNumeros = 4

    elif diaDaSemana == 'sexta':
        diaEmNumeros = 5

    elif diaDaSemana == 'sabado':
        diaEmNumeros = 6

    entrega = (diaEmNumeros + prazo) % 7

    if entrega == 0:
        print('sera entregue domingo')

    elif entrega == 1:
        print('sera entregue segunda')

    elif entrega == 2:
        print('sera entregue terca')

    elif entrega == 3:
        print('sera entregue quarta')

    elif entrega == 4:
        print('sera entregue quinta')

    elif entrega == 5:
        print('sera entregue sexta')

    elif entrega == 6:
        print('sera entregue sabado')
