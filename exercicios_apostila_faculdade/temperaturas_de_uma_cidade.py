def somatemp():
    soma = 0
    cont = 0
    while(cont <= 3):
        temp = float(input()) 
        soma += temp
        cont =+ 1
    return soma

S = somatemp()  
print(f"A soma das temperaturas é {S}")