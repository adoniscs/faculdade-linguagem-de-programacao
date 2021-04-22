nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome)) # alinha o nome a 20 espaços a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # alinha o nome a 20 espaços a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # centraliza o nome entre 20 espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)) # o nome fica entre o simbolo de = (igual)
