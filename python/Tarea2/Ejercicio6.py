'''
    Haz un programa que, dados cinco números introducidos por el
    usuario, determine cuál de los cuatro últimos números es más
    cercano al primero. Por ejemplo, si el usuario introduce 2,
    6, 4, 1 y 10, el programa responderá que "El número más cercano
    a 2 es 1"
'''

ref = int(input("Introduce el número de referencia: "))
n2 = int(input("Introduce segundo número: "))
n3 = int(input("Introduce tercer número: "))
n4 = int(input("Introduce cuarto número: "))
n5 = int(input("E introduce el quinto: "))
menor = 0

dif_2 = abs(ref - n2)
dif_3 = abs(ref - n3)
dif_4 = abs(ref - n4)
dif_5 = abs(ref - n5)

if dif_2 < dif_3:
    menor = str(n2) + ", segundo número"
elif dif_3 < dif_4:
    menor = str(n3) + ", tercer número"
elif dif_4 < dif_5:
    menor = str(n4) + ", cuarto número"
else:
    menor = str(n5) + ", quinto número "

print("El número más cercano es el " + str(menor))