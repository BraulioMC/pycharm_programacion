'''
    Haz un programa que implemente un cifrador de tipo César. Este tipo de
    cifrado consiste en sustituir cada letra del mensaje por la que se encuentra a un
    número establecido de posiciones, típicamente 3. Por ejemplo, se sustituye A por D,
    B por E, C por F,..., Z por C.

    El programa solicitará el texto a cifrar. Aceptará texto hasta que se introduzca la
    secuencia de caracteres “#FIN#”. A continuación, pedirá un número, que será la
    cantidad de letras de desplazamiento para el cifrado y mostrará por pantalla el
    criptograma resultante. Para su generación, ten en cuenta lo siguiente:

    ● El texto se convertirá a mayúsculas antes de su cifrado, de modo que el
    criptograma estará formado sólo por letras mayúsculas

    ● Sólo se cifrarán letras del alfabeto inglés, es decir, las existentes en ASCII.
    Cualquier otro carácter se mantendrá tal cuál en el criptograma.
    Recuerda que, en ASCII, la codificación de las letras es consecutiva

    ● El cifrado de una letra siempre tiene que ser otra letra del alfabeto

    ● El desplazamiento puede ser positivo o negativo

    Introduce el mensaje (#FIN# para terminar):
        ¡Esto es un mensaje sin cifrar!
        ¿Cómo lo ves?
        #FIN#

        Introduce el desplazamiento: 1
        Criptograma -->

        ¡FTUP FT VO NFOTBKF TJO DJGSBS!
        ¿DÓNP MP WFT?
'''

texto = ""

while True:
    print("Introduce texto a cifrar: ")
    texto = texto + input("> ")
    if texto.find("#FIN#") < 0:
        pass
    else:
        break


salida = ""
cesar = int(input("Introduce número de cifrado: "))
texto_mod = texto.upper()
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


for i in texto_mod:
    if i in mayusculas:
        valor = (int(ord(i)) + cesar)
        salida = salida + (chr(valor))
    else:
        salida = salida + i
print(salida)
