"""
faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Qual é o seu salário atual? R$'))
aumento_salario = salario + (salario * 15 / 100)
print('Bom... seu salário era de R${}, pois a partir de AGORA, passará a ser R${:.2f}. PARABÉNS! o/'.format(salario, aumento_salario))
print('Você teve um aumento de 15%, que será de R${:.2f}.'.format(aumento_salario - salario))