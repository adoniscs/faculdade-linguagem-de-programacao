# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um número: '))
print('Analisando o número {}, o seu dobro é {} o seu triplo é {} e a raiz quadrada é {:.1f}.'
      .format(numero, (numero*2), (numero*3), (numero ** (1/2))))
