'''
1.
Crea un módulo llamado t02_05_mod . Añade al módulo una función denominada
remove_dup que recibirá como argumento cualquier secuencia iterable (tupla, lista,
string,...) y devolverá como resultado una tupla con la secuencia original pero sin
duplicados.
Incluye en el d ocstring de la función los siguientes casos de uso:

Parámetro                       Resultado
[]                              ()
(1, 2, 3)                       (1, 2, 3)
(1, 2, 3, 2, 1)                 (1, 2, 3)
[1, (1, 2), 3, (1, 2), 4, 3]    (1, (1, 2), 3, 4)
"hooooooolaaaaa"                ('h', 'o', 'l', 'a')

2.
Añade al módulo una función denominada elimina_tildes_tup que, empleando tuplas ,
devuelva el texto recibido tras sustituir cada vocal con tilde, además de la la ü con
diéresis, por su correspondiente sin signo diacrítico.
Añade al docstring los correspondientes ejemplos de uso

3.
Añade al módulo una función denominada elimina_tildes que, empleando un único
diccionario , devuelva el texto recibido tras sustituir cada vocal con tilde, además de
la la ü con diéresis, por su correspondiente sin signo diacrítico.
Añade al docstring los correspondientes ejemplos de uso.
'''

# Creamos set para añadir elementos unicos, PRG_U2.05 pag 28/36

# Variables
# param1 = []
# param2 = (1, 2, 3)
# param3 = (1, 2, 3, 2, 1)
# param4 = [1, (1, 2), 3, (1, 2), 4, 3]
# param5 = "hooooooolaaaaa"

# Funcion
def remove_dup(arg):
    """Devuelve una tupla con lo que le pases.

        Args:
            arg (tuple, list): Tupla o lista con elementos posiblemente repetidos
        Returns:
            (tuple): Tupla con los elementos sin repetir

        Ejemplos:
            >>> remove_dup([])
            ()
            >>> remove_dup((1, 2, 3))
            (1, 2, 3)
            >>> remove_dup((1, 2, 3, 2, 1))
            (1, 2, 3)
            >>> remove_dup([1, (1, 2), 3, (1, 2), 4, 3])
            (1, (1, 2), 3, 4)
            >>> remove_dup("hooooooolaaaaa")
            ('h', 'o', 'l', 'a')
        """
    tmp = list()

    for i in arg:
        if i in tmp:
            pass
        else:
            tmp.append(i)
    salida = tuple(tmp)

    return salida

def elimina_tildes_tup(arg):
    '''
    Le pasamos una frase y devolvera lo mismo sin tilde ni dierisis en u
    :param arg: String
    :return: string

    Ejemplos:
        >>> elimina_tildes_tup("Hola que tal")
        'Hola que tal'
        >>> elimina_tildes_tup("Yo bien, y tú?")
        'Yo bien, y tu?'
        >>> elimina_tildes_tup("áéíóúü")
        'aeiouu'
    '''

    vocales = ("a", "e", "i", "o", "u", "u")
    tilde = ("á", "é", "í", "ó", "ú", "ü")
    salida = arg
    for i in arg:
        if i in tilde:
            if i == (tilde[0]):
                salida = salida.replace(i, vocales[0])
            elif i == (tilde[1]):
                salida = salida.replace(i, vocales[1])
            elif i == (tilde[2]):
                salida = salida.replace(i, vocales[2])
            elif i == (tilde[3]):
                salida = salida.replace(i, vocales[3])
            elif i == (tilde[4]):
                salida = salida.replace(i, vocales[4])
            elif i == (tilde[5]):
                salida = salida.replace(i, vocales[5])

    return str(salida)

def elimina_tildes(arg):
    '''
    Retora un string substituyendo vocales con tilde por vocales sin ella
    :param arg: string como una frase
    :return: mismo string sin tildes

    Ejemplos
        >>> elimina_tildes("Hola que tal")
        'Hola que tal'
        >>> elimina_tildes("Qué tal?")
        'Que tal?'
        >>> elimina_tildes("áéíóúü")
        'aeiouu'

    '''

    dic = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", "ü":"u"}
    salida = arg

    for i in arg:
        if (i in dic) == True:
            salida = salida.replace(i, dic[i])
    return salida


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# print("Parametro1 ->", remove_dup(param1))
# print("Parametro2 ->", remove_dup(param2))
# print("Parametro3 ->", remove_dup(param3))
# print("Parametro4 ->", remove_dup(param4))
# print("Parametro5 ->", remove_dup(param5))

# frase = input("Introduce frase:\n")
# print(elimina_tildes_tup(frase))