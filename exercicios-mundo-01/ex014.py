"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
"""
celcius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (9 * celcius / 5) + 32
print('A temperatura de {}ºC corresponde a {:.2f}ºF!'.format(celcius, fahrenheit))