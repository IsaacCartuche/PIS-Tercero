from modelo.docente import Docente
from controlador.dao.daoAdapter import DaoAdapter

class DocenteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Docente)
        self.__docente = None
        
    @property
    def _docente(self):
        if self.__docente == None:
            self.__docente = Docente()   
        return self.__docente
    
    @_docente.setter
    def _docente(self, value):
        self.__docente = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        lista = self._lista
        self._docente._id = lista._length + 1
        self._save(self._docente)
    
    def merge(self, pos):
        self._merge(self._docente, pos)
    
    def delete(self, pos):
        self._delete(self._docente, pos)