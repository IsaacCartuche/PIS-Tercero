from controlador.tda.linked.linkedList import Linked_List
from modelo.unidad import Unidad

class Criterios:
    def __init__(self):
        self.__id = 0
        self.__componenteEvaluado = ''
        self.__intrumentoEvaluado = ''
        self.__ponderaion = 0
        self.__total = 0
        self.__unidad = Unidad()
        self.__nota = Linked_List()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _componenteEvaluado(self):
        return self.__componenteEvaluado

    @_componenteEvaluado.setter
    def _componenteEvaluado(self, value):
        self.__componenteEvaluado = value

    @property
    def _intrumentoEvaluado(self):
        return self.__intrumentoEvaluado

    @_intrumentoEvaluado.setter
    def _intrumentoEvaluado(self, value):
        self.__intrumentoEvaluado = value

    @property
    def _ponderaion(self):
        return self.__ponderaion

    @_ponderaion.setter
    def _ponderaion(self, value):
        self.__ponderaion = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value
