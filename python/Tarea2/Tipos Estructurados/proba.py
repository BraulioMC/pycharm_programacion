import json, os

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
print(data)

var_json = json.loads(str(data))
