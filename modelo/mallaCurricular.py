from controlador.tda.linked import linkedList

class MallaCurricular:
    def __init__(self):
        self.__id = 0
        self.__descripcion = ''
        self.__pensum = ''
        self.__vigencia = bool
        self.__ciclo = linkedList()

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
    def _pensum(self):
        return self.__pensum

    @_pensum.setter
    def _pensum(self, value):
        self.__pensum = value

    @property
    def _vigencia(self):
        return self.__vigencia

    @_vigencia.setter
    def _vigencia(self, value):
        self.__vigencia = value

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

        