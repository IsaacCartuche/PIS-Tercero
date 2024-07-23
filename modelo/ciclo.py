from controlador.tda.linked.linkedList import Linked_List
from modelo.mallaCurricular import MallaCurricular
class Ciclo:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__materia = Linked_List()
        self.__mallaCurricular = MallaCurricular()

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
    def _materia(self):
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _mallaCurricular(self):
        return self.__mallaCurricular

    @_mallaCurricular.setter
    def _mallaCurricular(self, value):
        self.__mallaCurricular = value

        