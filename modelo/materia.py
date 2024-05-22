from modelo.asignacion import Asignacion
from modelo.ciclo import Ciclo

class Materia:
    def __init__(self):
        self.__id = None
        self.__nombre = ''
        self.__totalHoras = None
        self.__asignacion = Asignacion()
        self.__ciclo = Ciclo()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _totalHoras(self):
        return self.__totalHoras

    @_totalHoras.setter
    def _totalHoras(self, value):
        self.__totalHoras = value

    @property
    def _asignacion(self):
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value
