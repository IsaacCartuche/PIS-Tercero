from modelo.persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.__especialidad = ''
        self.__aniosExperienciaDocente = 0
        self.__cubiculo = ''
        self.__materia = ''

    @property
    def _materia(self):
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

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
            'nombre': self._nombre,
            'apellido': self._apellido,
            'correo': self._correo,
            'materia': self._materia,
            'ciclo': self._ciclo,
            'paralelo': self._paralelo,
            'tipoIdentificacion': self._tipoIdentificacion,
            'identificacion': self._identificacion,
            'telefono': self._telefono,
            'especialidad': self._especialidad,
            'aniosExperienciaDocente': self._aniosExperienciaDocente,
            'cubiculo': self._cubiculo
        }
    
    def deserializar(self, data):
        docente = Docente()
        docente._id = data['id']
        docente._nombre = data['Nombre']
        docente._apellido = data['Apellido']
        docente._correo = data['Correo']
        docente._materia = data['Materia']
        docente._ciclo = data['Ciclo']
        docente._paralelo = data['Paralelo']
        docente._tipoIdentificacion = data['tipoIdentificacion']
        docente._identificacion = data['identificacion']
        docente._telefono = data['telefono']
        docente._especialidad = data['especialidad']
        docente._aniosExperienciaDocente = data['aniosExperienciaDocente']
        docente._cubiculo = data['cubiculo']
        return docente
    