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

    @property
    def serialize(self):
        return {
            "id": self._id,
            "fechaInicio": self._fechaInicio,
            "fechaFin": self._fechaFin,
            "estadoActivo": self._estadoActivo,
            "cursa": self._cursa.serialize
        }
    def deserializar(self, data):
        periodo= Periodo()
        periodo._id = data['id']
        periodo._fechaInicio = data['fechaInicio']
        periodo._fechaFin = data['fechaFin']
        periodo._estadoActivo = data['estadoActivo']
        periodo._cursa = data['cursa']
        return periodo
