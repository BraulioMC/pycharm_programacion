'''
    Haz un programa que muestre la tabla de multiplicar de 0 a 10
    Su salida será:

    ***************************
    * TABLA DE MULTIPLICAR *
    ***************************
    ------------------------
        TABLA DEL: 0
    ------------------------
        0 x 0 = 0
        0 x 1 = 0
        ...
    ------------------------
        TABLA DEL: 10
    ------------------------
        10 x 0 = 0
        10 x 1 = 1
            ...
        10 x 10 = 100
    ------------------------
'''

print("*" * 27)
print("{}{:^25}{}".format("*", "TABLA DE MULTIPLICAR", "*"))
print("*" * 27, "\n")

for i in range(11):
    print("-" * 27)
    print("{:^27}".format("TABLA DEL " + str(i)))
    print("-" * 27)

    for j in range(11):
        cociente = (i * j)
        print("{:^27}".format(str(i) + " x " + str(j) + " = " + str(cociente)))
    print("\n")
