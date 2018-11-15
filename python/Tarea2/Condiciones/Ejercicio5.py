'''
    Haz un programa que calcule la menor de cinco palabras dadas, es decir, la
    primera de las cinco en orden alfabético. El programa no distinguirá entre
    mayúsculas y minúsculas
'''

palabra_1 = input("Introduce la primera palabra:\n-> ")
palabra_2 = input("Introduce la segunda palabra:\n-> ")
palabra_3 = input("Introduce la tercera palabra:\n-> ")
palabra_4 = input("Introduce la cuarta palabra:\n-> ")
palabra_5 = input("Introduce la quinta palabra:\n-> ")


menor = palabra_1

if palabra_2 < menor:
    menor = palabra_2
elif palabra_3 < menor:
    menor = palabra_3
elif palabra_4 < menor:
    menor = palabra_4
elif palabra_5 < menor:
    menor = palabra_5


print("La palabra menor es: " + menor)