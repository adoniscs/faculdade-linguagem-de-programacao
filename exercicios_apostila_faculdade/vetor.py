def conta(v, n, tam):
    cont = 0
    i = 0
    while i < tam:
        if v[i] == n:
            cont += 1
        i += 1
    return cont

a = [23, 4, 21, 3, 23]
num = int(input("Digite  o número a ser pesquisado: "))
contn = conta(a, num, 5)
print(f"O número foi encontrado {contn} vezes")
