import math

def dobro(x):
    return 2 * x

def saudacao(nome):
    print(f'Bem-vindo {nome}!')

nome = input('Qual o seu nome? ')
saudacao(nome)
dobro_n = int(input('Digite um número: '))
print(f'O dobro de {dobro_n} é {dobro(dobro_n)}')
