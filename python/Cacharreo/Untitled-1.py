import os

dic = {
    'nick': ['nick1', 'nick2'], 'nombre': ['nombre1', 'nombre2'], 'contact' : [('contacto1.0', 'contacto1.1'), ('contacto2.0','contacto2.1')]
}


os.system('cls||clear')
print(type(dic))
print(dic)

print(dic['nick'][0], dic['nombre'][0], dic['contact'][0])
