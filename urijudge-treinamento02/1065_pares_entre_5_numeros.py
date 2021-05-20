cont = 0
limit = 0

while limit < 5:
    n = int(input())
    if n % 2 == 0:
        cont += 1
    limit += 1
    
print(f'{cont} valores pares')
