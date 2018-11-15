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

#   Este tipo de control será de la siguiente forma:
'''
try:
    acciones que pueden generar un error
except tipo_de_error_1:
    acciones a ejecutar si se produce tipo_de_error_1
except tipo_de_error_2:
    acciones a ejecutar si se produce tipo_de_error_2
. . .
except :
    acciones a ejecutar si se produce un error no contemplado
else:
    acciones a ejecutar si no se produce ningún error
finally:
    acciones a ejecutar siempre (con o sin error)
'''
