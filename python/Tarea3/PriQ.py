class Tarea:
    _tid = 0

    def __init__(self, nom):
        Tarea._tid += 1
        self._id = Tarea._tid
        self.nom = nom 

    @property
    def id(self):
        return self._id

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    def __str__(self):
        return "(id:{}, '{}')".format(self._id, self._nom)

class PriQ:
    _PRI_MIN = 0    # Prioridad mínima
    _PRI_MAX = 5    # Prioridad máxima

    def __init__(self):
        self._tareas = {}

    def add(self, pri, tarea):
        if PriQ._PRI_MIN <= pri <= PriQ._PRI_MAX:
            if isinstance(tarea, Tarea):
                if pri in self._tareas:
                    self._tareas[pri].append(tarea)
                else:
                    self._tareas[pri] = [tarea]
            else:
                raise ValueError("'{}' no es una Tarea".format(tarea))
        else:
            raise ValueError("La prioridad:{} no es válida [0, 5 ]".format(pri))

    def get_tareas(self):
        if len(self):
            max_pri = sorted(self._tareas.keys())[-1]
            print("Prioridad máxima:", max_pri)
            print("Tareas:")
            for tarea in self._tareas[max_pri]:
                print(tarea)

    def __len__(self):
        cont = 0
        for t_lista in self._tareas.values():
            cont += len(t_lista)
        return cont

    def extraer(self):
        if len(self):
            max_pri = sorted(self._tareas.keys())[-1]
            tarea = self._tareas[max_pri].pop(0)
            if not len(self._tareas[max_pri]):
                del self._tareas[max_pri] 
            return tarea
        