'''
    Diseña un programa que pida dos números por teclado, determine si el primero
    es múltiplo del segundo y muestre el resultado de la siguiente forma:

    <num1> es múltiplo de <num2>
    <num1> no es múltiplo de <num2>
'''

num1 = float(input("Introduce número 1: "))
num2 = float(input("Introduce número 2: "))

if num1%num2 == 0 or num2%num1 == 0:
    print(str(num1) + " es múltiplo de " + str(num2))
else:
    print(str(num1) + " no es múltiplo de " + str(num2))