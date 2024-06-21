from modelo.estudiante import Estudiante
from controlador.dao.daoAdapter import DaoAdapter

class EstudianteControl(DaoAdapter):
    def __init__(self):
        super().__init__(Estudiante)
        self.__estudiante = None
        
    @property
    def _estudiante(self):
        if self.__estudiante == None:
            self.__estudiante = Estudiante()   
        return self.__estudiante
    
    @_estudiante.setter
    def _estudiante(self, value):
        self._estudiante = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        lista = self._lista
        self._estudiante._id = lista._length + 1
        self._save(self._estudiante)
    
    def merge(self, pos):
        self._merge(self._estudiante, pos)
    
    def delete(self, pos):
        self._delete(self._estudiante, pos)