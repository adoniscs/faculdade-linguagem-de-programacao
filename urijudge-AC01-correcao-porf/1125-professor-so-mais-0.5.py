trabalhos = float(input())
prova = float(input())

media = (trabalhos + prova) / 2

if media >= 6.0:
    print('aprovado')
else:
    media = (trabalhos + 10) / 2
    if media >= 6.0:
        print('talvez com sub')
    else:
        print('reprovado')
