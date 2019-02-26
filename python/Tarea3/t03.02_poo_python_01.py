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
        copia = str(self.value[:])
        return copia

    def __str__(self):
        return str(self.value)


lista_set = intSet()
print(lista_set)


lista_set.insert(55, -99, 0, 1)
print(lista_set)

lista_set.delete(55, 60, 1)
print(lista_set)

print(lista_set.copy)