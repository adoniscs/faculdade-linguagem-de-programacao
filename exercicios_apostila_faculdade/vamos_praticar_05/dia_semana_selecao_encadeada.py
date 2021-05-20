numero = int(input('Digite um número de 1 a 7: '))
dia = ''

if numero == 1:
    dia = 'domingo'
else:
    if numero == 2:
        dia = 'segunda'
    else:
        if numero == 3:
            dia = 'terca'
        else:
            if numero == 4:
                dia = 'quarta'
            else:
                if numero == 5:
                    dia = 'quinta'
                else:
                    if numero == 6:
                        dia = 'sexta'
                    else:
                        if numero == 7:
                            dia = 'sábado'
print(dia)
        
