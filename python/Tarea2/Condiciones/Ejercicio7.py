'''
    Haz un programa para calcular la letra del DNI. Solicitará al usuario la
    introducción del número de DNI (se comprobará que es de 8 dígitos)

    PISTA.
    El cálculo se hace de forma siguiente:
        - Dividimos el número DNI entre 23 y nos quedamos con el resto, que
        estará entre 0 y 22. Ese valor lo usaremos para obtener la letra a
        partir de la siguiente tabla:

+------------------------------------------------------------------------------------------------------------------+
| RESTO : | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
+------------------------------------------------------------------------------------------------------------------+
| LETRA : | t | r | w | a | g | m | y | f | p | d |  x |  b |  n |  j |  z |  s |  q |  v |  h |  l |  c |  k |  e |
+------------------------------------------------------------------------------------------------------------------+

'''

# Número de DNI

dni = int(input("Introduce número de DNI de 8 dígitos: "))

# Calculo

resto = int((dni % 23))
letra = "trwagmyfpdxbnjzsqvhlcke"


if len(str(dni)) != 8:
    print("Tiene que ser de 8 dígitos")
else:
    print("Calculando...")
    print(str(dni) + letra[resto])
