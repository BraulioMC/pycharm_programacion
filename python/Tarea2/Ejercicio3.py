'''
    Haz un programa que muestre el mayor de 3 números introducidos por el usuario
'''

print("Calcularemos el mayor de los tres números:")
print()

# Introducir numeros
# Si no es un numero pide meter un numerico
num1 = input("Introduce primer número: ")
while not str.isdigit(num1):
    num1 = input("Que sea un número: ")

num2 = input("Introduce el segundo: ")
while not str.isdigit(num2):
    num2 = input("Que sea un número: ")

num3 = input("Introduce el tercero: ")
while not str.isdigit(num3):
    num3 = input("Que sea un numero: ")


mayor = num1

if num2 > mayor:
    mayor = num2
elif num3 > mayor:
    mayor = num3

print("El mayor es: " + mayor)