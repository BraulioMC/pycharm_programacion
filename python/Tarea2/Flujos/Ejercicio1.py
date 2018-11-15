'''
    Escribe un programa que pida al usuario un número entre 0 y 9
    y muestre su tabla de multiplicar
'''

import sys

try:
    num = int(input("Introduce un número: "))

    for i in range(11):
        producto = (num * i)
        print(
            str(num) + " * " + str(i) + " = " + str(producto)
        )
except ValueError:
    sys.exit("No pueden ser letras")