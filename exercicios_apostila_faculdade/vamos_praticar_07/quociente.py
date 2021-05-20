"""
Crie um programa que solicite ao usuário dois números naturais x e y, o programa
deverá exibir o quociente da divisão inteira de x por y sem usar os operadores de
divisão e multiplicação. Por exemplo, se x=7 e y=2 a resposta será 3, pois podemos
raciocinar que o quociente da divisão inteira de x por y é dado pela quantidade de vezes
que y pode ser subtraído de x sem que x se torne negativo
"""
x = int(input('x: ')) # dividendo
y = int(input('y: ')) # divisor
quociente = 0

while x >= y:
    x -= y
    quociente += 1

print(f'O quociente é {quociente}')
