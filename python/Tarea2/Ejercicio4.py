'''
    Haz un programa para resolver ecuaciones de segundo grado de la forma:

    a*x^2 + b*x + c = 0, donde las soluciones son x = (−b ±√b2−4·a·c)/2*a

    El programa pedirá al usuario los coeficientes a, b y c y mostrará, o bien las
    soluciones con dos decimales de precisión, o un mensaje informando al usuario del
    error correspondiente

    Debes tener en cuenta que:
        ● El coeficiente a tiene que ser distinto de 0
        ● Si el discriminante ( b^2 − 4 · a · c ) es negativo, no tiene soluciones reales
        ● Si el discriminante es 0, sólo tiene una solución

    Para realizar la raíz cuadrada, tienes dos opciones:
        ● elevar a una potencia de 0.5
        ● usar la función sqrt() de la librería math . Esta función devuelve el resultado de
        aplicar la raíz cuadrada al número pasado como argumento. Añade al
        principio del código la sentencia de importación de la librería ( import math ) y
        llámala anteponiendo el nombre de la librería ( math.sqrt())
'''

while True:
    try:
        coef_a = int(input("Introduce coeficiente a que no sea cero: "))
        while coef_a == 0:
            print("No puede ser cero")
            int(input("Introduce entero distinto de 0: "))
        break
    except (ValueError):
        print("No es un numero entero")

while True:
    try:
        coef_b = int(input("Introduce coeficiente b: "))
        break
    except (ValueError):
        print("No es un numero entero")

while True:
    try:
        coef_c = int(input("Introduce coeficiente c: "))
        break
    except (ValueError):
        print("No es un numero entero")

