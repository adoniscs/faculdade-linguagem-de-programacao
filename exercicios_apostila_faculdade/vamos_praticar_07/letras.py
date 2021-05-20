letra = input('digite uma letra diferente de "x" para continuar: ')
cont = 0

while letra != 'x':
    cont += 1
    letra = input('digite outra letra diferente de "x" para continuar: ')
print(f'Foram digitadas {cont} letras')
