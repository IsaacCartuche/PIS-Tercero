from modelo.persona import Persona
from controlador.tda.linked import linkedList

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.__matricula = None
        self.__cursa = linkedList()

    @property
    def _cursa(self):
        return self.__cursa

    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value

    @property
    def _matricula(self):
        return self.__matricula

    @_matricula.setter
    def _matricula(self, value):
        self.__matricula = value
