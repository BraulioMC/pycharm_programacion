class Hechizo(object):
    def __init__(self, conjuro, nombre):
        self.nombre = nombre
        self.conjuro = conjuro

    def __str__(self):
        return self.nombre + ' ' + self.conjuro + '\n' + self.getDescripcion()

    def getDescripcion(self):
        return 'Sin descripcion'

    def ejecutar(self):
        print(self.conjuro)

class Accio(Hechizo):
    def __init__(self):
        Hechizo.__init__(self, 'Accio', 'Encantamiento convocador')

class Confundo(Spell):
    def __init__(self):
        Hechizo.__init__(self, 'Confundo', 'Encantamiento Confundus')

    def getDescription(self):
        return 'Causa confusión en la víctima.'

    def examinarHechizo(hechizo):
        print(hechizo)

hechizo = Accio()
hechizo.ejecutar()
examinarHechizo(hechizo)
examinarHechizo(Confundo())

