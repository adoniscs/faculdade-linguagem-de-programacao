"""
Crie uma função que receba como argumento um número natural n e 
devolva um valor booleano indicando se n é primo”. Um número natural 
é considerado primo se possui exatamente dois divisores naturais, o
número 1 e o próprio n
"""

def primo(n):
    qtd_divisores = 0
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            qtd_divisores += 1
        divisor += 1

    if qtd_divisores == 2:
        return True
    else:
        return False
