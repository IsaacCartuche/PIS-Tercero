from modelo.persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.__especialidad = ''
        self.__aniosExperienciaDocente = 0
        self.__cubiculo = ''

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
    def _cubiculo(self):
        return self.__cubiculo

    @_cubiculo.setter
    def _cubiculo(self, value):
        self.__cubiculo = value

    @property
    def serializer(self):
        return{
            'id': self._id,
            'tipoIdentificacion': self._tipoIdentificacion,
            'identificacion': self._identificacion,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'telefono': self._telefono,
            'especialidad': self._especialidad,
            'aniosExperienciaDocente': self._aniosExperienciaDocente,
            'cubiculo': self._cubiculo
        }
    
    def deserializar(self, data):
        docente = Docente()
        docente._id = data['id']
        docente._tipoIdentificacion = data['tipoIdentificacion']
        docente._identificacion = data['identificacion']
        docente._nombre = data['nombre']
        docente._apellido = data['apellido']
        docente._telefono = data['telefono']
        docente._especialidad = data['especialidad']
        docente._aniosExperienciaDocente = data['aniosExperienciaDocente']
        docente._cubiculo = data['cubiculo']
        return docente
    