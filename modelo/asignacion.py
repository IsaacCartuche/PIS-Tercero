from modelo.cursa import Cursa
from controlador.tda.linked import linkedList

class Asignacion:
    def __init__(self):
        self.__id = None
        self.__cedula = ''
        self.__cursa = Cursa()
        self.__materia = linkedList()
        self.__unidad = linkedList()

    @property
    def _materia(self):
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value

    @property
    def _cursa(self):
        return self.__cursa

    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value
