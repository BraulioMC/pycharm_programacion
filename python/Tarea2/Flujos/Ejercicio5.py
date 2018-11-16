'''
    Escribe un programa que solicite al usuario que escriba una frase, la imprima al
    revés y nos diga cuántas palabras contiene. Ten en cuenta que podría haber más de
    un espacio en blanco entre algunas de las palabras
'''


frase = input("Escribe una frase: ")

# tmp1 = len(frase)
tmp2 = frase.split()
count = 0

for i in tmp2:
    count = count + 1

print("{}{}{}{}".format("Total: ", count, " palabras ", tmp2))
