def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(f'{4} é par? {par(4)}')
print(f'{7} é par? {par(7)}')


def soma(n1, n2):
    print('Início do bloco da função')
    s = n1 + n2
    return s

print('Fora da função')

print('-' * 20)

def diga_ola():
    print(f'Olá {nome}') # acessa a variável global

nome = 'Mega' # variável global
diga_ola()

print('-' * 20)

def diga_ola(nome):
    print(f'Olá {nome}!')

nome = 'Megan'
diga_ola('Maria')
print(f'Tchau {nome}!')

print('-' * 20)

def diga_ola():
    global nome, titulo         # são identificadores globais
    print(f'Olá {titulo} {nome}')
    nome = 'Megan'
    titulo = 'Sra.'

titulo = 'Dra.'
nome = 'Maria'
diga_ola()
print(f'Tchau {titulo} {nome}')
