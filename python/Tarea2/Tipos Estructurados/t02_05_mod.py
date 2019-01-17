'''
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
'''

# Creamos set para añadir elementos unicos, PRG_U2.05 pag 28/36

# Variables
param1 = []
param2 = (1, 2, 3)
param3 = (1, 2, 3, 2, 1)
param4 = [1, (1, 2), 3, (1, 2), 4, 3]
param5 = "hooooooolaaaaa"

# Funcion
def remove_dup(arg):
    tmp = list()

    for i in arg:
        if i in tmp:
            pass
        else:
            tmp.append(i)
    salida = tuple(tmp)

    return salida

print("Parametro 1 ->", remove_dup(param1))
print("Parametro 2 ->", remove_dup(param2))
print("Parametro 3 ->", remove_dup(param3))
print("Parametro 4 ->", remove_dup(param4))
print("Parametro 5 ->", remove_dup(param5))