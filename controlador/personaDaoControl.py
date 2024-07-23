from modelo.persona import Persona
from controlador.dao.daoAdapter import DaoAdapter

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Persona)
        self.__persona = None
        
    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()   
        return self.__persona
    
    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        lista = self._lista
        self._persona._id = lista._length + 1
        self._save(self._persona)
    
    def merge(self, pos):
        self._merge(self._persona, pos)
    
    def delete(self, pos):
        self._delete(self._persona, pos)