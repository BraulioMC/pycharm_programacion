'''
02.05 - Python Tipos estructurados
'''

'''

lista = [1,2,3,4,5,6]
print(lista)

# Eliminamos la posicion 1
lista.pop(lista[1])
print(lista)

# Añadimos una lista dentro de otra lista
lista += [['a','b','c']]
print(lista)

# Recorremos lista
for element in [1, 2, 3]:
    print(element)

# Recorremos tupla
for element in (1, 2, 3):
    print(element)


for key in {'one':1, 'two':2}:
    print(key)

# Recorremos string
for char in {'123'}:
    print(char)

# Recorremos ficheros
for line in open("myfile.txt"):
    print(line, end='')
'''
## Array esta en deshuso

import array

a = array.array('B',[1,2,3,4])
a.append(255) # Maximo 255 por el tipo de dato

print(a)
