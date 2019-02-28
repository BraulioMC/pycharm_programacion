from menu import MenuGen, Entrante, Carne, Pescado
import os
import platform

def clear_screen():
    """Limpia la consola.

    Se identifica el sistema operativo anfitrión para invocar el comando adecuado.
    """
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux' or sistema == 'Darwin':
        os.system('clear')

def wait_enter():
    """Espera un [enter] para continuar."""
    print("\nPulsa [RET] para continuar")
    input()

def get_opc(options):
    """Muestra el menú y captura una la opción seleccionada.
    
    Params:
        options (dict): Diccionario de opciones
    """

    opts = list(options.keys())

    # Capturar la opción
    while True:
        # Mostrar el menú
        clear_screen()
        print("========== M E N U ==========\n")
        for k, v in options.items():
            print(" {}:\t{}".format(k, v))

        opc = input("\n> Opción: ").upper()
        if opc in opts:
            break

    return opc

def nuevo_plato(mg):
    while True:
        clear_screen()
        tipo = input("Elige un tipo de plato ([E]ntrante, [P]escado, [C]arne): ").upper()
        if tipo in "EPC":
            break              
        
    nom = input("\nNombre del plato: ")        

    # Añadimos un nuevo objeto del tipo correspondiente a la lista de platos
    if tipo == "E":
        plato = Entrante(nom)
    elif tipo == "P":
        plato = Pescado(nom)
    else:
        plato = Carne(nom)
        
    clear_screen()
    if mg.add_plato(plato):
        print("\nNuevo plato añadido")
    else:
        print("\nNo se añadió el plato !!!")

def eliminar_plato(mg):
    while True:
        nom = input("\nNombre del plato (L - mostrar lista): ")   
        if nom[0].upper() == "L":
            mg.show_platos()
        elif len(nom):
            break

    clear_screen()
    if mg.del_plato(nom):
        print("\nPlato eliminado")
    else:
        print("\nNo hay platos con el nombre indicado")    

def main():
    """Bucle principal."""

    options = {'N':'Nuevo plato', 'E':'Eliminar plato', 'L':'Lista de platos', 'G':'Genera menú', 'S':'Salir'}

    # Objeto principal generador de menús
    mg = MenuGen()

    while True:
        try:
            clear_screen()
            opc = get_opc(options)
            if opc == 'S':
                exit(0)
            elif opc == 'N':
                # nuevo plato
                clear_screen()
                nuevo_plato(mg)
            elif opc == 'E':
                # eliminar plato
                clear_screen()
                eliminar_plato(mg)                
            elif opc == 'L':
                # listado de platos
                clear_screen()
                mg.show_platos()
            elif opc == 'G':
                # generar menú
                clear_screen()
                mg.gen_menu()
            wait_enter()
        except (KeyboardInterrupt, EOFError):
            exit(0)
        except Exception as e:
            clear_screen()
            print(e)
            wait_enter()

if __name__ == "__main__":
    main()