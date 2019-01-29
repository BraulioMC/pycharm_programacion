class Rectangulo(object):
    """Clase de prueba para tener un rectangulo"""
    
    def __init__(self, y, x, ancho, alto):
        self.y = y
        self.x = x
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return (self.ancho * self.alto)

    def __str__(self):
        '''Muestra el Rectangulo'''
        return "Alto: %s, Ancho: %s, Coordenadas iniciales: %s . %s" % (self.alto, self.ancho, self.y, self.x)


Rectangulo.area(0, 0, 10, 20)
