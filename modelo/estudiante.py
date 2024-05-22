from modelo.persona import Persona
from controlador.tda.linked.linkedList import Linked_List

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.__matricula = None
        self.__cursa = Linked_List()

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

    @property
    def serializer(self):
        return{
            'id': self._id,
            'cedula': self._cedula,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'fechaNacimiento': self._fechaNacimiento,
            'telefono': self._telefono,
            'direccion': self._direccion,
            'matricula': self._matricula,
            'cursa': self._cursa
        }
    
    def deserializar(self, data):
        estudiante = Estudiante()
        estudiante._id = data['id']
        estudiante._cedula = data['cedula']
        estudiante._nombre = data['nombre']
        estudiante._apellido = data['apellido']
        estudiante._fechaNacimiento = data['fechaNacimiento']
        estudiante._telefono = data['telefono']
        estudiante._direccion = data['direccion']
        estudiante._matricula = data['matricula']
        estudiante._cursa = data['cursa']
        return estudiante
    