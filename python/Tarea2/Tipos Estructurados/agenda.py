'''
Crea un programa para gestionar una agenda de json_body. El programa contará con un
menú con las siguientes opciones:

● N - Nuevo contacto: solicitará los datos de un nuevo contacto. Los datos estarán
formados por:
    ○ nick (str), que utilizaremos como identificador/clave del contacto
    ○ nombre (str), nombre y apellidos
    ○ métodos de contacto (list), lista con los diferentes formas de contactar con el
    contacto (teléfonos, direcciones de e-mail, direcciones,...)

● E - Eliminar contacto: eliminará un contacto de la agenda tras solicitar su nick

● A - Añadir tlf/e-mail/dir: nos permitirá añadir nuevos métodos de contacto en una
entrada de la agenda

● M - Mostra agenda: listará los json_body (y sus datos) de la agenda ordenado
alfabéticamente

● B - Buscar contacto: permitirá buscar los datos de un contacto a través de su nick

● G - Grabar agenda: permitirá almacenar los cambios realizado en un archivo JSON.
Para la lectura/escritura de la agenda en archivos JSON se emplearán las funciones
load_dict_json( ) y write_dict_json( ) proporcionadas

● S - Salir: finalizará el programa
Ten en cuenta que:
    ● Puedes implementar la agenda como un diccionario donde nick es la clave de cada
    entrada. El valor de cada una de ellas será una lista que contenga el nombre del
    contacto y la lista de métodos de contacto
    agenda = { nick : [ nombre, [ métodos de contacto ] ] }
    ● Al iniciarse el programa, lo primero que debería hacer, es cargar en la agenda los
    datos existentes en el archivo JSON
    ● Debes tener en cuenta que, inicialmente, tu agenda puede estar vacía. Debes
    asegurar que estos no provoque errores al lanzar las diferentes opciones del menú.
    ● Del mismo modo, debes tratar de garantizar el cierre ordenado de la aplicación
    cuando en la entrada de datos se produzcan interrupciones del tipo ^C o similar
    ● Ten en cuenta que, las búsquedas por clave en el diccionario, cuando esta clave no
    existe, generan errores que deberías evitar o controlar
'''
import os, json

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

def new_contact():
    path = "F:\\braulio.mosquera\\Documents\\DAW\\pycharm_programacion\\python\\Tarea2\\Tipos Estructurados\\agenda.json"
    nick = input("NICK: ")
    nombre = input("NOMBRE: ")
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
    
    data = {}
    data['NICK'] = nick
    data['NOMBRE'] = nombre
    data['CONTACTO'] = contacto
    with open(path, 'w') as outfile:
        json.dump(json.dumps(data), outfile)
    

def select_option():
    print(draw_menu())
    varOption = input('Introduce una opcion: ')
    varOption = varOption.upper()

    if varOption == "N":
        os.system('cls||clear')
        print("Nuevo contacto")
        new_contact()

    elif varOption == "E":
        print("opcion E")
    elif varOption == "A":
        print("opcion A")
    elif varOption == "M":
        print("opcion M")
    elif varOption == "B":
        print("opcion B")
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


while True:
    print(select_option())