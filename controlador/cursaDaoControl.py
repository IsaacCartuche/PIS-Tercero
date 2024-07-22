from typing import TypeVar, Generic, Type
from controlador.dao.daoAdapter import DaoAdapter
from modelo.cursa import Cursa
from controlador.tda.linked.linkedList import Linked_List
from json.os import json
class CursaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Cursa)
        self._cursa = None# Carga los datos del archivo en la lista enlazada

    @property
    def _cursa(self):
        if self.__curso == None:
            self._cursa = Linked_List()
            self._cursa.load()
        return self._cursa
    
    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value

    @property
    def list(self):
        return self._cursa
 
    @property
    def save(self):
        self._cursa._id = self._cursa._id + 1
        #print("cursaaa")
        #print(self._cursa.serialize)
        self._cursa.save(self._cursa.serialize)

    def marge (self, pos):
        self._cursa.marge(self.__cursa,pos)