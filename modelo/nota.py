from modelo.criterios import Criterios
from datetime import date
class Nota:
    def __init__(self):
        self.__id = 0
        self.__descripcion = ''
        self.__calificacion = 0
        self.__fecha = date()
        self.__criterios = Criterios()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    @property
    def _calificacion(self):
        return self.__calificacion

    @_calificacion.setter
    def _calificacion(self, value):
        self.__calificacion = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _criterios(self):
        return self.__criterios

    @_criterios.setter
    def _criterios(self, value):
        self.__criterios = value
