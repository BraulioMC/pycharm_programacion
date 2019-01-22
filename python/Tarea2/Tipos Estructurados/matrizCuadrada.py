'''
Crea un programa que permita crear y editar una matriz cuadrada de NxM celdas. El
programa contará con un menú con las siguientes opciones:
● I - Iniciar matriz: solicitará el número de filas y de columnas de la matriz y el valor
inicial para las celdas
● M - Mostrar matriz: mostrará el valor actual de las celdas de la matriz
● C - Cambiar valor: permitirá modificar el valor de una celda concreta. Para ello
solicitará la fila, la columna y el nuevo valor
● S - Salir: finalizará el programa

Se tendrá en cuenta que:
● Podemos implementar una matriz NxM como una lista que contenga N listas de M
elementos cada una
● Cuando se inicialice la matriz, se verificará que el número de filas y columnas estará
entre 1 y 99
● Cuando se modifique una celda, se verificará que los números de fila y columna son
válidos.
● Se controlará el cierre ordenado de la aplicación si se produce un ^C en cualquier
momento
● Sólo podremos mostrar la matriz o cambiar el valor de una de sus celdas si la matriz
ha sido inicializada previamente
'''

import os

def crea_lista(filas, columna):
    lista = []
    celdas = columna*filas
    for i in range(0, celdas):
        lista.append(0.0)
    return lista

def crear_matriz(colum, files, lista):
    files += 1
    count = 0
    var = True
    varCount = 0

    while (count < files):
        if var:
            print(" " * 4, end="")
            for i in range(colum):
                print('{}{:^5}'.format("|", i), end="")
            var = False

        else:
            print('{}{:^3}'.format(" ", (count)-1), end="")
            for i in range(colum):
                print('{}{:^5}'.format("|", lista[varCount]), end="")
                varCount += 1
        print("")

        print(("-"*5) + ("-"*5)*colum + "-"*5)
        count += 1
    return lista

def modificar_matriz(fila, columna, lista, valor, numColum):
    if (fila == 0):
        lista[columna] = valor
    else:
        numLista_mod = (fila * numColum) + columna
        lista[numLista_mod] = valor
    return lista

while True:
    print('''
        ######## M A T R I X ########
            I: Iniciar Matriz
            M: Mostrar matriz
            C: Cambiar valor
            S: Salir
    ''')
    select = input("> Opcion: ")

    if (select == "I" or select == "i"):
        varFiles = int(input("Numero de filas: "))
        varColum = int(input("Numero de columnas: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        lista = crea_lista(varFiles, varColum)

        crear_matriz(varFiles, varColum, lista)
    elif (select == "M" or select == "m"):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            crear_matriz(varFiles, varColum, lista)
        except NameError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("La matriz no esta inicializada")

    elif (select == "C" or select == "c"):
        varFiles_mod = int(input("Numero fila: "))
        varColum_mod = int(input("Numero columna: "))
        varValor_mod = float(input("Nuevo valor: "))

        os.system('cls' if os.name == 'nt' else 'clear')
        lista = (modificar_matriz(varFiles_mod, varColum_mod, lista, varValor_mod, varColum))
        crear_matriz(varFiles, varColum, lista)
    elif (select == "S" or select == "s"):
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Elige un valor válido")

