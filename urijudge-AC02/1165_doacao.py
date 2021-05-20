moedaVC = float(input())
contVC = 0
contR = 0
total = 0

while moedaVC != -1:
    total = moedaVC * 2.50
    contVC += moedaVC
    contR += total
    moedaVC = float(input())

print(f'VC$ {contVC:.2f}')
print(f'R$ {contR:.2f}')
