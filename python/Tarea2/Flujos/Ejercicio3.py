'''
    Diseña un programa que solicite al usuario un número entero positivo y
    determine si es un número primo o no.


num = int(input("Introduce número: "))

if num < 1:                             #si es menos que 2 no es primo
    print(str(num) + "No es primo")
elif num % num == 0:                    #si el resto da 0 no es primo
    print(str(num) + " no es primo")
'''

# -*- coding: utf-8 -*-


def es_primo(numero):
    """
        Funcion que determina si un numero es primo
        Tiene que recibir el numero entero

        Para que un numero sea primo, unicamente tiene que dividirse dos veces:
        1 - divisible entre 1
        2 - divisible entre el mismo
        En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
        que si en el bucle, alguna vez se divide el numero, quiere decir que no es
        primo
    """

    for i in range(2, numero):
        if (numero % i) == 0:
            # es divisible
            return False    # Retorna un valor bool true o false para la salida del programa
    return True             # Este valor bool, se usará en el if para mostrar uno y otro valor

while True:
    try:
        numero = int(input("inserta un numero, (0) salir >> "))
        if numero == 0:
            break
        if es_primo(numero):
            print("\nEl numero %s es primo" % numero)
        else:
            print("\nEl numero %s NO es primo" % numero)
    except:
        print("\nEl numero tiene que ser entero o no contener letras")
