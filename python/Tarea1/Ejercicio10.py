'''
    Diseña un programa que solicite el lado mayor y menor de un rectángulo
    y calcule su área y perímetro. La salida de los valores numéricos debe
    ser con dos decimales de pecisión y deben quedar alineados por la dere
    cha según el ejemplo de ejecución
'''

lado_1 = float(input("Introduce uno de los lados: "))
lado_2 = float(input("Introduce el otro lado: "))

perimetro = float(lado_1 * 2 + lado_2 * 2)
area = float(lado_1 * lado_2)



print()

print("=" * 36)
print("{0:<26}{1:>10}".format("Perímetro del rectángulo: " , perimetro))
print("{0:<26}{1:>10}".format("Área del rectángulo: ", area))
print("=" * 36)
