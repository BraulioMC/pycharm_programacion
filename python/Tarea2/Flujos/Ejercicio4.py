'''
    Modifica el programa para que devuelva todos los números primos entre 1
    y el número introducido por el usuario
'''

num = int(input("Introduce número: "))

if num < 1:                             #si es menos que 2 no es primo
    print(str(num) + "No es primo")
for i in range(2, num):                 #un rango desde el dos hasta el numero que nosotros elijamos
    if num % i == 0:                    #si el resto da 0 no es primo
        print(str(i) + " no es primo")
print(str(num) + " es primo")           #de lo contrario devuelve Verdadero

