from typing import Type
from controlador.dao.daoAdapter import DaoAdapter
from models.periodo import Periodo

class PeriodoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Periodo)
        self._list() # Carga los datos del archivo en la lista enlazada

    @property
    def list(self):
        
        return self.lista