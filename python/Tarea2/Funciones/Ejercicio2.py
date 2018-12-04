'''
	Crea un programa que dibuje figuras. Se podrá seleccionar entre dos tipos de figuras, el cuadrado y el triángulo.
	Cada tipo de figura será dibujada por una función diferente. En ambos casos se pedirá la altura de la figura y
	el carácter utilizado para rellenarla. El programa se seguirá ejecutando hasta que se presione CTRL-C,
	en que mostrará un mensaje de despedida y finalizará
'''


try:
    print("========== EL FIGURILLAS ==========")
    print("Vamos a dibujar figuras ( CTRL-C para terminar )")
    selecion = int(input("Escoge el tipo (1 - Cuadrado, 2 - Triángulo): "))
    altura = int(input("Cuál es la altura: "))
    relleno = input("Y el relleno: ")
except ValueError:
    print("Debe ser un número")
    exit()

try:
    if selecion == 1:
        for i in range(altura):
            print((relleno + " ") * altura)
    elif selecion == 2:
        cont = 1
        formato = ("{:^" + str(altura * altura//2) + "}")
        for i in range(altura):
            print(formato.format((relleno + " ") * cont))
            cont += 1
    else:
        print("Debes seleccionar entre valor 1 y 2")
except NameError:
    pass