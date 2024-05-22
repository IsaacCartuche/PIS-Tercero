from modelo.asignacion import Asignacion
from controlador.tda.linked.linkedList import Linked_List
from modelo.estadistica import Estadistica

class Unidad:
    def __init__(self):
        self.__id = 0
        self.__promedio = 0
        self.__asignacion = Asignacion()
        self.__criterios = Linked_List()
        self.__estadistica = Estadistica()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _promedio(self):
        return self.__promedio

    @_promedio.setter
    def _promedio(self, value):
        self.__promedio = value

    @property
    def _asignacion(self):
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value

    @property
    def _criterios(self):
        return self.__criterios

    @_criterios.setter
    def _criterios(self, value):
        self.__criterios = value

    @property
    def _estadistica(self):
        return self.__estadistica

    @_estadistica.setter
    def _estadistica(self, value):
        self.__estadistica = value
