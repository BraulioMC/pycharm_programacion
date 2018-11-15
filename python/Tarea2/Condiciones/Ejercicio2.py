'''
    Haz un programa que solicite al usuario la entrada de un número entero y diga
    si es par o impar. El programa mostrará alguno de los siguientes mensajes:

    El valor <valor_introducido> no es us numérico
    0 es un númro par
    <valor_introducido> es un número par
    <valor_introducido> es un número impar
'''

numero = input("Introduce un numero: ")

if str.isdigit(numero):
    if int(numero) % 2 == 0:
        print("El valor " + numero + " es un número par")
    else:
        print("El valor " + numero + " no es un número par")
else:
    print("El valor " + numero + "no es numérico")
