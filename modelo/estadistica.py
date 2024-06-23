from modelo.unidad import Unidad
from modelo.informe import Informe
class Estadistica:
    def __init__(self):
        self.__id = 0
        self.__titulo = ''
        self.__unidad = Unidad()
        self.__informe = Informe()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _titulo(self):
        return self.__titulo

    @_titulo.setter
    def _titulo(self, value):
        self.__titulo = value

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _informe(self):
        return self.__informe

    @_informe.setter
    def _informe(self, value):
        self.__informe = value

    def serealizar(self):
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "unidad": self.__unidad,
            "informe": self.__informe
        }
    
