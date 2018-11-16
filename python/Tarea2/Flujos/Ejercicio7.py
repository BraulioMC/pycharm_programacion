'''
    Diseña un programa que, en primer lugar, le pida al usuario que escriba un
    carácter cualquiera (letra, dígito,...). A continuación, aceptará entradas del usuario
    hasta que éste escriba la secuencia “<>”. Por último, mostrará cuántas ocurrencias
    del carácter se produjeron en el texto introducido hasta la aparición de dicha
    secuencia.
'''

count = 0

while True:
    digito = input("Introduce caracter a buscar: ")
    if len(digito) != 1:
        print("Debe ser sólo un dígito...")
    else:
        break

while True:
    cadena = input("Escribe lo que quieras (<> para Finalizar)")
    count = count + cadena.count(digito)
    if cadena.find("<>") < 0:                                       # Si no encuentra <>, la salida es -1
        pass                                                        # Cuando la condicion encuentra <> hace break
    else:
        break

print("\nTenemos " + str(count) + " digitos \"" + str(digito) + "\" encontrados en la conversación")