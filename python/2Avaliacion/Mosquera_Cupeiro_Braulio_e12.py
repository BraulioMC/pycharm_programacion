import Mosquera_Cupeiro_Braulio_1 as mcb
import random

while True:
    try:
        num_mejillones = int(input("Cuantos mejillones vas a comer [Ctrl-C para salir]: "))
    except KeyboardInterrupt:
        exit(0)

    n = 0
    lista = []

    while n < num_mejillones:
        lista.append(random.randint(1, 9))

        n += 1

    print("Los tamaños son: ", lista)

    monton = mcb.hoy_comemos_mejillones(tuple(lista))

    print("Montones resultantes: ", monton)