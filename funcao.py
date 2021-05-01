def bem_vindo():
    print('Bem Vindo! Vamos calcular a média.')
    return

def retorna_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

bem_vindo()

print('Digite o primeiro valor')
n1 = float(input())

print('Digite o segundo valor')
n2 = float(input())

print('Digite o terceiro valor')
n3 = float(input())

resp = retorna_media(n1, n2, n3)

print(f'A média é {resp:.2f}')