from controlador.tda.linked.linkedList import Linked_List
from modelo.proyecciones import Proyecciones
class Informe:
    def __init__(self):
        self.__id = 0
        self.__descripcion = ''
        self.__estadistica = Linked_List()
        self.__proyecciones = Proyecciones()


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
    def _estadistica(self):
        return self.__estadistica

    @_estadistica.setter
    def _estadistica(self, value):
        self.__estadistica = value

    