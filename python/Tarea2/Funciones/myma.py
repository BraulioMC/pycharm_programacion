'''
Modulo de funciones
'''

def es_par(numero):
    '''Determina si un numero es par

    Args:
        numero (int): numero entero para determinar
    Returns:
        (bool): True or False
    '''

    if int(numero) % 2 == 0:
        print("El valor " + str(numero) + " es un número par")
        return True
    else:
        print("El valor " + str(numero) + " no es un número par")
        return False


def ecu_1g():
    '''Resuelve ecuaciones de 1er grado'''

def ecu_2g():
    '''Resuelve ecuaciones de 2do grado'''

def es_primo():
    '''Determina si un numero es primo'''

def fibo():
    '''Calcula serie Fibonacci'''

if __name__ == "__main__":
    import sys
    es_par(int(sys.argv[]))