'''
Para cada una de las siguientes expresiones, especifica su tipo y valor. Si genera un error,
indica tipo 'NoneType' y escribe 'error' en la columna del valor. Si el método no genera
ninguna salida, indica ‘NoneType’ como tipo y ‘None’ como valor
Supón que se ha realizado la siguiente asignación:
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
Asume que las siguientes operaciones se realizan en el orden indicado:
'''

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
listA.sort()
listA
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
listA
listA + listB
listB.sort()
listB.pop()
listB.count( ' a ' )
listB.remove( ' a ' )
listA.extend([4,1,6,3,4])
listA.count(4)
listA.index(1)
listA.pop(4)
listA.reverse()
listA
print(type(listA))
print(listA)

'''
Expresión                       Tipo            Valor
----------------------------------------------------------------+
listA.sort()                |   NoneType    |   None            |
listA                       |   list        |   [1, 4, 3, 0]    |
listA.insert(0, 100)        |   NoneType    |   None
listA.remove(3)             |   NoneType    |   None
listA.append(7)             |   NoneType    |   None
listA                       |   
listA + listB               |   
listB.sort()                |   
listB.pop()                 |   
listB.count( ' a ' )        |   
listB.remove( ' a ' )       |   
listA.extend([4,1,6,3,4])   |   
listA.count(4)              |   
listA.index(1)              |   
listA.pop(4)                |   
listA.reverse()             |   
listA                       |   
-----------------------------------------------------------------+
'''