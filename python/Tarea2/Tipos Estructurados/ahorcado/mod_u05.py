import json
import pickle
import os
import platform


def clear_screen():
    """Limpia la consola.

    Se identifica el sistema operativo anfitrión para invocar el comando adecuado.
    """
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux' or sistema == 'Darwin':
        os.system('clear')


def write_dict_json(d, file_name):
    """Almacena el diccionario como un archivo JSON.

    Args:
        d (dict): diccionario
        file_name (str): nombre del archivo
    """
    with open(file_name, mode='w') as file:
        file.write(json.dumps(d))


def load_dict_json(file_name):
    """Lee un diccionario almacenado como archivo JSON.

    Args:
        file_name (str): nombre del archivo
    Returns:
        (dict): diccionario
    """
    d = {}
    try:
        with open(file_name, mode='r') as file:
            d = json.loads(file.read())
    except FileNotFoundError:
        pass
    return d


def write_dict_bin(d, file_name):
    """Almacena el diccionario como un archivo binario.

    Args:
        d (dict): diccionario
        file_name (str): nombre del archivo
    """
    with open(file_name, mode='wb') as file:
        pickle.dump(d, file)


def load_dict_bin(file_name):
    """Lee un diccionario almacenado como archivo binario.

    Args:
        file_name (str): nombre del archivo
    Returns:
        (dict): diccionario
    """
    d = {}
    try:
        with open(file_name, mode='rb') as file:
            d = pickle.load(file)
    except FileNotFoundError:
        pass
    return d


def load_words(file_name="words.txt"):
    """Lee una lista de palabras de un archivo.

    Se supone que sólo hay una palabra por línea.

    Args:
        file_name (str): nombre del archivo
    Returns:
        (tuple): colección de palabras
    """
    lista = []

    try:
        with open(file_name, mode='r') as file:
            s = file.readline().strip()
            while s != "":
                s = elimina_tildes(s)
                lista.append(s)
                s = file.readline().strip()
    except FileNotFoundError:
        pass

    return tuple(lista)


def elimina_tildes(s):
    """Sustituye las vocales con tilde.

    Params:
        s (str): texto con "posibles" tildes
    Returns:
        (str): devuelve el texto sin tildes
    """
    tildes = {'Á': 'A', 'á': 'a', 'É': 'E', 'é': 'e', 'Í': 'I', 'í': 'i',
              'Ó': 'O', 'ó': 'o', 'Ú': 'U', 'ú': 'u', 'Ü': 'U', 'ü': 'u'}

    for k in tildes:
        s = s.replace(k, tildes[k])

    return s


def get_hang_pic():
    """Devuelve una colección de pics para el programa hangman.

    Returns:
        (tuple): colección de pics
    """
    return (
    """ 
        ┳━━━━┓
        ┆    ┃
             ┃        
             ┃
             ┃
             ┃
             ┃
             ┃
             ┃
      ━━━━━━━┻
    """,
    """ 
        ┳━━━━┓
        ┆    ┃
        ☹    ┃
             ┃
             ┃
             ┃             
             ┃
             ┃
             ┃
      ━━━━━━━┻
    """,
    """ 
        ┳━━━━┓
        ┆    ┃
        ☹    ┃
       ⎛⋂⎞   ┃
             ┃
             ┃             
             ┃
             ┃
             ┃
      ━━━━━━━┻
    """,
    """ 
        ┳━━━━┓
        ┆    ┃
        ☹    ┃
       ⎛⋂⎞   ┃
       ⎝⋃⎠   ┃
             ┃
             ┃
             ┃
             ┃
      ━━━━━━━┻
    """,
    """ 
        ┳━━━━┓
        ┆    ┃
        ☹    ┃
       ⎛⋂⎞   ┃
       ⎝⋃⎠   ┃
       ⎧ ⎫   ┃
             ┃       
             ┃
             ┃
      ━━━━━━━┻
    """,
    """ 
        ┳━━━━┓
        ┆    ┃
        ☹    ┃
       ⎛⋂⎞   ┃
       ⎝⋃⎠   ┃
       ⎧ ⎫   ┃
       │ │   ┃
             ┃       
             ┃
      ━━━━━━━┻
    """,
    """ 
        ┳━━━━┓
        ┆    ┃
        ☹    ┃
       ⎛⋂⎞   ┃
       ⎝⋃⎠   ┃
       ⎧ ⎫   ┃
       │ │   ┃
       ⎭ ⎩   ┃
             ┃
      ━━━━━━━┻
    """)

