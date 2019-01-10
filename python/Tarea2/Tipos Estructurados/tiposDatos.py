'''
Para cada una de las siguientes expresiones, especifica su tipo y valor. Si genera un error,
selecciona el tipo 'NoneType' y escribe 'error' en la columna del valor.
Supón que se ha realizado la siguiente asignación:
x = (1, 2, (3, 'Juan', 4), 'Hola')
'''

x = (1, 2, (3, 'Juan', 4), 'Hola')

print(type(x[2][2]))
print(type(x[-1]))

'''
Expresión   Tipo        Valor
x[0]        int         1
x[2]        tuple       (3, 'Juan', 4)
x[-1]       
x[2][2]     str         'Juan'
x[2][-1]    
x[-1][-1]   
x[-1][2]    
x[0:1]      
x[0:-1]
len(x)
2 in x
3 in x
x[0] = 8
'''
