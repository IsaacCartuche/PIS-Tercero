from modelo.cursa import Cursa
from datetime import date
class Periodo:
    def __init__(self):
        self.__id = 0
        self.__fechaInicio = date()
        self.__fechaFin = date()
        self.__estadoActivo = bool
        self.__cursa = Cursa()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fechaInicio(self):
        return self.__fechaInicio

    @_fechaInicio.setter
    def _fechaInicio(self, value):
        self.__fechaInicio = value

    @property
    def _fechaFin(self):
        return self.__fechaFin

    @_fechaFin.setter
    def _fechaFin(self, value):
        self.__fechaFin = value

    @property
    def _estadoActivo(self):
        return self.__estadoActivo

    @_estadoActivo.setter
    def _estadoActivo(self, value):
        self.__estadoActivo = value

    @property
    def _cursa(self):
        return self.__cursa

    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value

        