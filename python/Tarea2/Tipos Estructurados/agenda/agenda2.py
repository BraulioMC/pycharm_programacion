import mod_u05
import os

path = (os.path.dirname(os.path.abspath(__file__)) + "\\agenda2.json")

if not os.path.exists(path):
    f = open(path, "w+")
    f.write('{}')

if __name__ == "__main__":
    # Preparar diccionario
    mod_u05.clear_screen()
    dic=mod_u05.load_dict_json(path)

    # Añadir contacto nuevo
    while True:
        dic2 = mod_u05.select_option(dic, path)
        dic = dic2

    # Escribir dic en json
    # mod_u05.write_dict_json(dic, path)
