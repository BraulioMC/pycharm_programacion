class IntSet:
    def __init__(self, val=None):
        """Constructor de la instancia.
        
        Params:
            val (int, list, set, tuple): valores de inicialización
        """
        self._set = []
        if val:
            if isinstance(val, (list, tuple, set)):
                for item in val:
                    self.insert(item)
            else:
                self.insert(val)

    def get_set(self):
        """Devuelve una copia de la lista."""
        return tuple(sorted(self._set))

    def insert(self, val):
        """Inserta un nuevo entero en la lista si no está repetido.
        
        Params:
            val (int) : nuevo entero
        Raises:
            (ValueError) : si val no es entero
        """
        if isinstance(val, int):
            if val not in self._set:
                self._set.append(val)
        else:
            raise ValueError("<" + str(val) + "> no es un entero")
        
    def remove(self, val):
        """Elimina un elemento de la lista.
        
        Params:
            val (int) : valor a eliminar
        Raises:
            (KeyError) : si val no está en la lista
        """
        try:
            self._set.remove(val)
        except:
            raise KeyError("<" + str(val) + "> no está en en el conjunto")

    def copy(self):
        """Devuelve una copia del objeto.
        
        Returns:
            (IntSet)
        """
        return IntSet(self.get_set())

    def union(self, other):
        """Devuelve un IntSet con la unión.
        
        Params:
            other (IntSet): instancia de IntSet
        Returns:
            (IntSet): nuevo Intset            
        """                   
        if isinstance(other, IntSet):
            return IntSet(set(self.get_set()) | set(other.get_set()))
        else:
            raise ValueError("<" + str(other) + "> no es un IntSet")

    def intersect(self, other):
        """Devuelve un IntSet con la intersección.
        
        Params:
            other (IntSet): instancia de IntSet
        Returns:
            (IntSet): nuevo Intset            
        """     
        if isinstance(other, IntSet):
            return IntSet(set(self.get_set()) & set(other.get_set()))
        else:
            raise ValueError("<" + str(other) + "> no es un IntSet")        

    def subtract(self, other):
        """Devuelve un IntSet con la diferencia.
        
        Params:
            other (IntSet): instancia de IntSet
        Returns:
            (IntSet): nuevo Intset                      
        """
        if isinstance(other, IntSet):
            return IntSet(set(self.get_set()) - set(other.get_set()))
        else:
            raise ValueError("<" + str(other) + "> no es un IntSet")     

    def clear(self):
        """Vacía el conjunto."""
        self._set = []

    def __eq__(self, other):
        """Chequea si dos objetos IntSet son iguales.

        Params:
            other (IntSet): instancia de IntSet
        Returns:
            (bool): True si contienen los mismos elementos. False si no
        Raises:
            (ValueError): si other no es IntSet
        """
        if isinstance(other, IntSet):
            return sorted(self._set) == sorted(other._set)
        else:
            raise ValueError("<" + str(other) + "> no es un IntSet")  

    def __contains__(self, val):
        """Chequea si val está en la lista.
        
        Params:
            val (int): valor a chequear
        Returns:
            (boolean): True si está. False si no
        """
        return val in self._set

    def __len__(self):
        """Devuelve el número de enteros en el set.
        
        Returns:
            (int): número de elementos
        """
        return len(self._set)

    def __str__(self):
        """String representando al objeto.
        
        Returns:
            (str): string con la lista ordenada con formato "{val1, val2,... }"
        """
        if len(self._set):
            s = "{"
            for x in sorted(self._set):
                s += str(x) + ", "
            return s[:-2] + "}"
        else:
            return "{}"

    def __repr__(self):
        return "IntSet(" + self.__str__() + ")"
            
    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self._set):
            self._n += 1
            return self._set[self._n-1]
        else:
            raise StopIteration

