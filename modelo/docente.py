from modelo.persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.__especialidad = ''
        self.__aniosExperienciaDocente = 0

    @property
    def _especialidad(self):
        return self.__especialidad

    @_especialidad.setter
    def _especialidad(self, value):
        self.__especialidad = value

    @property
    def _aniosExperienciaDocente(self):
        return self.__aniosExperienciaDocente

    @_aniosExperienciaDocente.setter
    def _aniosExperienciaDocente(self, value):
        self.__aniosExperienciaDocente = value

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
            'especialidad': self._especialidad,
            'aniosExperienciaDocente': self._aniosExperienciaDocente
        }
    
    def deserializar(self, data):
        docente = Docente()
        docente._id = data['id']
        docente._cedula = data['cedula']
        docente._nombre = data['nombre']
        docente._apellido = data['apellido']
        docente._fechaNacimiento = data['fechaNacimiento']
        docente._telefono = data['telefono']
        docente._direccion = data['direccion']
        docente._especialidad = data['especialidad']
        docente._aniosExperienciaDocente = data['aniosExperienciaDocente']
        return docente
    