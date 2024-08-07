from modelo.persona import Persona
#from controlador.tda.linked.linkedList import Linked_List

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.__matricula = 0
        self.__fechaNacimiento = ''
        #self.__cursa = Linked_List()

    @property
    def _matricula(self):
        return self.__matricula

    @_matricula.setter
    def _matricula(self, value):
        self.__matricula = value

    @property
    def _fechaNacimiento(self):
        return self.__fechaNacimiento

    @_fechaNacimiento.setter
    def _fechaNacimiento(self, value):
        self.__fechaNacimiento = value

    """ @property
    def _cursa(self):
        return self.__cursa

    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value """



    @property
    def serializer(self):
        return{
            'id': self._id,
            'tipoIdentificacion': self._tipoIdentificacion,
            'identificacion': self._identificacion,
            'correo': self._correo,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'telefono': self._telefono,
            'ciclo': self._ciclo,
            'paralelo': self._paralelo,
            'matricula': self._matricula,
            'fechaNacimiento': self._fechaNacimiento,
            #'cursa': self._cursa
        }
    
    def deserializar(self, data):
        estudiante = Estudiante()
        estudiante._id = data['id']
        estudiante._tipoIdentificacion = data['tipoIdentificacion']
        estudiante._identificacion = data['identificacion']
        estudiante._correo = data['Correo']
        estudiante._nombre = data['Nombre']
        estudiante._apellido = data['Apellido']
        estudiante._telefono = data['telefono']
        estudiante._ciclo = data['Ciclo']
        estudiante._paralelo = data['Paralelo']
        estudiante._matricula = data['matricula']
        estudiante._fechaNacimiento = data['fechaNacimiento']
        #estudiante._cursa = data['cursa']
        return estudiante
    