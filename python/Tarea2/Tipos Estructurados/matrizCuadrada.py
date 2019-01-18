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

def crear_matriz(colum, files):
    lista = []
    celdas = colum*files
    files += 1
    count = 0
    var = True
    varCount = 0

    for i in range(0, celdas):
        lista.append(0.0)

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
    return ""



varFiles = int(input("Numero de filas: "))
varColum = int(input("Numero de columnas: "))

print(crear_matriz(varFiles,varColum))

print("Cambiemos un valor")
files = int(input("Numero fila: "))
colum = int(input("Numero columna: "))



