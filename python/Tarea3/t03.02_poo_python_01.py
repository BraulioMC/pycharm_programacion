class intSet():
    def __init__(self, *args):
        self._value = set(args)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = set(value)

    def insert(self, *args):
        for i in args:
            self._value.add(i)
    
    def delete(self, *args):
        for i in args:
            try:
                self._value.remove(i)
            except KeyError as e:
                print('No encontrado: ', e)

    def copy(self):
        copia = str(self.value)
        return copia
    
    def get_set(self):
        return tuple(sorted(self.value))

    def __str__(self):
        return str(self.value)


# Crea instancia de la clase intSet
list_numeros = intSet()
print(list_numeros)

# Inserta numeros
list_numeros.insert(55, -99, 0, 1)
print(list_numeros)

# Borra un numero
list_numeros.delete(55, 60, 1)
print(list_numeros)

# Copia
print("Copia -> ", list_numeros.copy())

# Tupla ordenada
print(list_numeros.get_set())

