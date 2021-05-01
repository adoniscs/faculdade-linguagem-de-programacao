nt_trabalho = float(input())
nt_prova = float(input())
sub = 10

media = (nt_trabalho + nt_prova) / 2
media2 = (media + sub) / 2

if media >= 6:
    print('aprovado')
elif nt_trabalho > 2 and media2 >= 6:
    print('talvez com a sub')
else:
    print('reprovado')


