class Agenda:
    def __init__(self):
        self.lista = []
    
    def __str__(self):
        return self.lista

class Contacto(Agenda):
    def __init__(self, nom, tlf):
        Agenda.__init__(self)

        self.nombre = nom
        self.telefono = tlf
        self.correo = ""
        self.nacimiento = ""
    
    def getNac(self):
        return self.nacimiento
    
    def setNac(self, fnac):
        self.nacimiento = fnac
    
    def nuevo_contacto(self, valor):
        if isinstance(valor, Agenda):
           self.lista.append(valor)
    
    
class Persona(Contacto):
    def __init__(self, nom, tlf):
        Contacto.__init__(self, nom, tlf)
    
    def __str__(self):
        return self.nombre


class Trabajo(Contacto):
    def __init__(self, nom, tlf):
        self.empresa = ""
        Contacto.__init__(self, nom, tlf)
    
    def getEmpresa(self):
        return self.empresa
    
    def setEmpresa(self, emp):
        self.empresa = emp

