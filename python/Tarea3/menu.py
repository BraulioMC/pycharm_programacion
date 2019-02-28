import random

class Plato:
    def __init__(self, nom):
        self._nom = nom
    
    @property
    def nombre(self):
        return self._nom

class Entrante(Plato):
    def __str__(self):
        return "(E) " + self._nom

class Carne(Plato):
    def __str__(self):
        return "(C) " + self._nom

class Pescado(Plato):
    def __str__(self):
        return "(P) " + self._nom

class MenuGen:
    def __init__(self):
        """Inicializador."""
        self._platos = {'E':[], 'P':[], 'C':[]}

    def add_plato(self, plato):
        """Añade un nuevo plato a la lista de platos correspondiente."""
        ret = False

        if isinstance(plato, Entrante):
            self._platos['E'].append(plato)
            ret = True
        elif isinstance(plato, Pescado):
            self._platos['P'].append(plato)
            ret = True
        elif isinstance(plato, Carne):
            self._platos['C'].append(plato)            
            ret = True

        return ret

    def del_plato(self, nom):
        """Elimina un plato de la lista."""
        encontrado = False

        for lista_platos in self._platos.values():
            for plato in lista_platos:
                if plato.nombre == nom:
                    lista_platos.remove(plato)
                    encontrado = True
                    break

        return encontrado

    def gen_menu(self):
        """Genera un nuevo menú."""

        # Chequeamos que haya platos suficientes
        for lista_platos in self._platos.values():
            if len(lista_platos)<2:
                raise Exception("No hay platos suficientes para generar un menú")
        
        # Generamos el menú
        print("-"*40)      
        print("MENU")
        print("Primeros:")
        for plato in random.sample(self._platos['E'], 2):
            print("\t" + str(plato))
        print("Segundos:")
        print("\t" + str(random.choice(self._platos['P'])))
        print("\t" + str(random.choice(self._platos['C'])))      
        print("-"*40)      

    def show_platos(self):
        """Imprime el listado de platos."""
        print("-"*40)      
        print("PLATOS")

        print("Entrantes")
        for plato in self._platos['E']:
            print("\t" + str(plato))

        print("Pescados")
        for plato in self._platos['P']:
            print("\t" + str(plato))

        print("Carnes")
        for plato in self._platos['C']:
            print("\t" + str(plato))                                

        print("-"*40)                  

