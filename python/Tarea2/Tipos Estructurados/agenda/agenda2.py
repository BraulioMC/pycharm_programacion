import mod_u05
import os

path = (os.path.dirname(os.path.abspath(__file__)) + "\\agenda2.json")

if not os.path.exists(path):
    f = open(path, "w+")
    f.write('{}')


# Parte 0 - Pintar menu

# mod_u05.select_option()

# Parte 1 - Preparar diccionario
mod_u05.clear_screen()
dic=mod_u05.load_dict_json(path)

dic2 = mod_u05.select_option()
dic.update(dic2)

# Parte 2 - Escribir dic en json
mod_u05.write_dict_json(dic, path)

