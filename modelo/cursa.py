from modelo.estudiante import Estudiante
from modelo.periodo import Periodo
from controlador.tda.linked import linkedList

class Cursa:
    def __init__(self):
        self.__id = None
        self.__paralelo = ''
        self.__estudiante = Estudiante()
        self.__periodo = Periodo()
        self.__asignacion = linkedList()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value

    @property
    def _estudiante(self):
        return self.__estudiante

    @_estudiante.setter
    def _estudiante(self, value):
        self.__estudiante = value

    @property
    def _periodo(self):
        return self.__periodo

    @_periodo.setter
    def _periodo(self, value):
        self.__periodo = value

    @property
    def _asignacion(self):
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value
