def imprime():
    print(f'pagamento: {cont}')
    print(f'antes = {antes}')
    print(f'depois = {total_divida}')
    print('-----')


total_divida = int(input())
pagar_mes = int(input())
cont = 0

while total_divida > 0:
    cont += 1
    antes = total_divida
    total_divida -= pagar_mes

    if antes < pagar_mes:
        total_divida = 0
        
    imprime()
