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

def new_contact(dic1):
    dic2 = {}
    nick = input("NICK: ")
    nombre = [input("NOMBRE: ")]
    contacto = []

    while True:
        try:
            add_contact = input("CONTACTO: ")
            if len(add_contact) != 0:
                contacto.append(add_contact)
            else:
                break
        except KeyboardInterrupt:
            os.system('cls||clear')
            break
    
    nombre.append(contacto)
    dic2[nick] = nombre

    dic1.update(dic2)

    return dic1

def draw_menu():
    os.system('cls||clear')
    menu = (
        "########## MENU ##########\n"
        "N - Nuevo contacto\n"
        "E - Eliminar contacto\n"
        "A - Añadir tlf/e-mail/dir\n"
        "M - Mostra agenda\n"
        "B - Buscar contacto\n"
        "G - Grabar agenda\n"
        "S - Salir\n"
    )
    return menu

def select_option(dic):
    print(draw_menu())
    varOption = input('Introduce una opcion: ')
    varOption = varOption.upper()

    if varOption == "N":
        os.system('cls||clear')
        print("Nuevo contacto")
        dic = new_contact(dic)

    elif varOption == "E":
        os.system('cls||clear')
        print("Elimina nick")
        dic = elimina_nick(dic)

    elif varOption == "A":
        os.system('cls||clear')
        print("Añade contactos")
        dic = añade_contactos(dic)

    elif varOption == "M":
        os.system('cls||clear')
        print("Mostrar agenda")
        muestra_agenda(dic)

    elif varOption == "B":
        os.system('cls||clear')
        print("Buscar contacto")
        buscar_contacto(dic)

    elif varOption == "G":
        print("opcion G")
    elif varOption == "S":
        os.system('cls||clear')
        print("Bye!")
        exit()
    else:
        os.system('cls||clear')
        print("La opcion introducida no es valida")
        exit()

    return dic

def elimina_nick(dic):
    nick = input('Indica nick: ')
    dic.pop(nick)
    return dic

def añade_contactos(dic):
    nick = input("Indica Nick: ")
    while True:
        try:
            add_contact = input("CONTACTO: ")
            if len(add_contact) != 0:
                dic[nick][1].append(add_contact)
            else:
                break

        except KeyboardInterrupt:
            os.system('cls||clear')
            break
    
    return dic

def muestra_agenda(dic):
    keylist = dic.keys()
    sorted(keylist)
    
    for key in keylist:
        print("Nick: {} - Contacto: {}".format(key, dic[key]))

def buscar_contacto(dic):
    nick = input("Indica Nick: ")
    print(dic[nick])

