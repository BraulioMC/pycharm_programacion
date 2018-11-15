'''
    Si buscamos que la entrada solo sé un número, nos puede dar un
    error si introducimos letras. El error en este mismo caso será
    ValueError.

    Le decimos que si es ValueError nos muestre una print
'''

try:
    num = int(input("Introduce un número: "))
    if num%2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")
except ValueError:
    print("Valor no válido")