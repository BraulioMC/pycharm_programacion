import json, os
class Agenda:

    def __init__(self, *args, **kwargs):
        self.nick = args
        self.nombre = args
        self.contacto = []
        self.path = os.path.dirname(os.path.abspath(__file__))

        fn = self.path + "\\agenda.json"
        try:
            agenda_data = open(fn, 'r')
        except IOError:
            agenda_data = open(fn, 'w')
    
    def menu(self):
        opcion = ''
        os.system('cls||clear')
        while opcion != 'S':
            print("########## MENU ##########")
            print("N - Nuevo contacto")
            print("E - Eliminar contacto")
            print("A - Añadir tlf/e-mail/dir")
            print("M - Mostra agenda")
            print("B - Buscar contacto")
            print("G - Grabar agenda")
            print("S - Salir")
            opcion = input("\nIngrese su opcion:")
            opcion = opcion.upper()
            print(opcion)

            if opcion == "N":
                os.system('cls||clear')
                print("Nuevo contacto")
                self.__append_contact()
            elif opcion == "E":
                print("opcion E")
            elif opcion == "A":
                print("opcion A")
            elif opcion == "M":
                print("opcion M")
            elif opcion == "B":
                print("opcion B")
            elif opcion == "G":
                print("opcion G")
            elif opcion == "S":
                os.system('cls||clear')
                print("Bye!")
                exit()
                # return super().__init__(*args, **kwargs)
    
    def __append_contact(self):
        nick = input('Nick: ')
        nombre = input('Nombre: ')
        contacto = []

        while True:
            add_contact = input("CONTACTO: ")
            if len(add_contact) != 0:
                contacto.append(add_contact)
            else:
                break
        
        dic_agenda = json.loads(self.path)
        print(dic_agenda)

        for i in range(0, 3):
            print(i)
        
        print(nick, nombre, str(contacto))
        # self.__init__()


agenda = Agenda()
agenda.menu()