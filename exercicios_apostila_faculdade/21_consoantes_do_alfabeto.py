def consoantes():
    codigo_unicode = ord('a')
    while codigo_unicode <= ord('z'):
        letra = chr(codigo_unicode)
        if (letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u'):
            print(letra)
        codigo_unicode += 1
