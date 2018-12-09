'''
Modulo de funciones
'''

def es_par(numero):
    '''Determina si un numero es par

    Args:
        numero (int): numero entero para determinar
    Returns:
        (bool): True or False
    Error:
        (str): Devuelve E si hubo un error
    >>> es_par(13)
    False

    >>> es_par(4)
    True

    >>> es_par("par")
    E
    '''

    if int(numero) % 2 == 0:
        return True
    else:
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
    try:
        import sys
        salida = es_par(int(sys.argv[1]))

        if salida:
            print("Es par")
        else:
            print("Es impar")
    except:
        print("E")