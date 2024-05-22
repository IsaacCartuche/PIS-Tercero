from modelo.informe import Informe

class Proyecciones:
    def __init__(self):
        self.__resultado = ''
        self.__informe = Informe()

    @property
    def _resultado(self):
        return self.__resultado

    @_resultado.setter
    def _resultado(self, value):
        self.__resultado = value

    @property
    def _informe(self):
        return self.__informe

    @_informe.setter
    def _informe(self, value):
        self.__informe = value
