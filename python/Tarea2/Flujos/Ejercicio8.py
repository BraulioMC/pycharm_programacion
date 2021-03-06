'''
    Si te fijas en la codificación ASCII de las letras, se puede observar cómo la
    diferencia entre una letra mayúscula y su correspondiente minúscula, está en el bit 6

    A → 65 10 → 0b1 0 00001
    a → 97 10 → 0b1 1 00001
    B → 66 10 → 0b1 0 00010
    b → 98 10 → 0b1 1 00010
    C → 67 10 → 0b1 0 00011
    c → 99 10 → 0b1 1 00011

    Haz un programa que acepte un texto por teclado y, usando las operaciones de nivel
    de bit, convierta cada carácter al contrario. El cambio sólo debería afectar a los
    caracteres alfabéticos

    PISTA:
    Recuerda que la función predefinida ord(c) nos devuelve el valor Unicode de un
    carácter. Es la inversa de la función chr(n). Por ejemplo, ord(“A”) devuelve 65 y
    chr(65) sería igual a “A”
'''


texto = "Hola que tal estamos 64564"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
salida = ""

for i in texto:
    pos = (len(bin(ord(i))) - 6)
    binario = bin(ord(i))
    tmp = (binario[pos])

    if i in minusculas or i in mayusculas:
        if tmp == str(0):
            salida = salida + (chr(ord(i) + 32))
        else:
            salida = salida + (chr(ord(i) - 32))
    else:
        salida = salida + i

print(salida)