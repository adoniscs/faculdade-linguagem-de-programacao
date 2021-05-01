"""
escreva um programa que faça o computador "pensar" em 
um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever na tela se 
o usuário venceu ou perdeu.
"""

numero = 5
print('Pensei em um número, adivinhe qual é!')
numero_user = int(input('Digite o numero: '))

if numero_user == numero:
    print('VENCEU!')
else:
    print('PERDEU')
