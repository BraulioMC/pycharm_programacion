'''
	A partir del código del programa del cálculo de la letra de DNI, crea una función llamada calcula_letra_DNI que
	reciba como parámetro el númro de DNI y devuelva:
		●	La letra del DNI si todo fue correcto
		●	El valor "ERR" si no se pudo calcular debido a que el argumento era incorrecto
	
	Crea un programa que llame a la función con valores correctos e incorrecto de número de DNI para probarla en
	diferentes situaciones

+------------------------------------------------------------------------------------------------------------------+
| RESTO : | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
+------------------------------------------------------------------------------------------------------------------+
| LETRA : | t | r | w | a | g | m | y | f | p | d |  x |  b |  n |  j |  z |  s |  q |  v |  h |  l |  c |  k |  e |
+------------------------------------------------------------------------------------------------------------------+
'''

def calcula_letra_DNI(numero):
    resto = int((numero % 23))
    letra = "trwagmyfpdxbnjzsqvhlcke"
    dni = letra[resto]
    return dni

# Número de DNI
numero = int(input("Introduce número de DNI de 8 dígitos: "))


if len(str(numero)) != 8:
    print("Tiene que ser de 8 dígitos")
else:
    print("Calculando...")
    dni = calcula_letra_DNI(numero)
    print(str(numero )+ str(dni))
