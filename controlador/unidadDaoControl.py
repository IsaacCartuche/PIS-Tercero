from controlador.dao.daoAdapter import DaoAdapter
from modelo.unidad import Unidad 
class UnidadDaoControl(DaoAdapter):
    def __init__(self,):
        super().__init__(Unidad)
        self.__unidad = Unidad()
        

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._persona._id = self._lista._length + 1
        self._save(self._persona)