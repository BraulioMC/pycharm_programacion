'''
    Haz un programa que muestre el mayor de 3 números introducidos por el usuario
'''

print("Calcularemos el mayor de los tres números:")
print()

# Primer numero
num1 = input("Introduce primer número: ")

while not str.isdigit(num1):
    num1 = input("Que sea un número: ")

# Segundo número
num2 = input("Introduce el segundo: ")

while not str.isdigit(num2):
    num2 = input("Que sea un número: ")

# Segundo número
num3 = input("Introduce el tercero: ")

while not str.isdigit(num3):
    num3 = input("Que sea un numero: ")


if num1 > num2:
    if num1 > num3:
        print("El mayor es: " + num1)
    else:
        print("El mayor es: " + num3)
else:
    if num2 > num3:
        print("El mayor es: " + num2)
    else:
        print("El mayor es: " + num3)
