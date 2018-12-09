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
    import sys
    salida = es_par(int(sys.argv[1]))

    if salida:
        print("Es par")
    else:
        print("Es impar")