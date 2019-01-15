'''
Para cada una de las siguientes expresiones, especifica su tipo y valor. Si genera un error,
selecciona el tipo 'NoneType' y escribe 'error' en la columna del valor.
Supón que se ha realizado la siguiente asignación:
x = (1, 2, (3, 'Juan', 4), 'Hola')
'''

x = (1, 2, (3, 'Juan', 4), 'Hola')

# print(type(x[2][2]))
print(3 in x)
print(2 in x)

'''
Expresión   Tipo        Valor
x[0]        int         1
x[2]        tuple       (3, 'Juan', 4)
x[-1]       str         Hola
x[2][2]     str         'Juan'
x[2][-1]    int         4
x[-1][-1]   str         a
x[-1][2]    str         l
x[0:1]      int         1
x[0:-1]     tuple       1,
len(x)      int         4
2 in x      True        True
3 in x      False       False
x[0] = 8    error       error
'''
