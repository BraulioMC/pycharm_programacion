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
        coef_a = float(input("Introduce coeficiente a que no sea cero: "))
        while coef_a == 0:
            print("No puede ser cero")
            float(input("Introduce entero distinto de 0: "))
        break
    except (ValueError):
        print("No es un numero entero")

while True:
    try:
        coef_b = float(input("Introduce coeficiente b: "))
        break
    except (ValueError):
        print("No es un numero entero")

while True:
    try:
        coef_c = float(input("Introduce coeficiente c: "))
        break
    except (ValueError):
        print("No es un numero entero")


#   Cerebro del ejercicio


from math import sqrt

if coef_a != 0:
    x_1 = (- coef_b + sqrt(coef_b ** 2 - 4 * coef_a * coef_c)) / (2 * coef_a)
    x_2 = (- coef_b - sqrt(coef_b ** 2 - 4 * coef_a * coef_c)) / (2 * coef_a)
    print('Soluciones de la ecuacion: x1=%4.2f y x2=%4.2f ' % (x_1, x_2))
else:
    if coef_b != 0:
        x_3 = -coef_c / coef_b
        print('Solucion de la ecuacion: x=%4.2f ' % x_3)
    else:
        if coef_c != 0:
            print('La ecuacion no tiene solucion. ')
        else:
            print('La ecuacion tiene infinitas soluciones. ')


