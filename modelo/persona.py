from modelo.cuenta import Cuenta

class Persona:
    def __init__(self):
        self.__id = 0
        self.__tipoIdentificacion = ''
        self.__identificacion = ''
        self.__nombre = ''
        self.__apellido = ''
        self.__telefono = ''
        self.__ciclo = ''
        self.__paralelo = ''
        
        self.__cuenta = Cuenta()

    @property
    def _cuenta(self):
        return self.__cuenta

    @_cuenta.setter
    def _cuenta(self, value):
        self.__cuenta = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value

    @property
    def _identificacion(self):
        return self.__identificacion

    @_identificacion.setter
    def _identificacion(self, value):
        self.__identificacion = value

    @property
    def _correo(self):
        return self.__cuenta._correo

    @_correo.setter
    def _correo(self, value):
        self.__cuenta._correo = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value


        
    @property
    def serialize(self):
        return{
            'id': self._id,
            'tipoIdentificacion': self._tipoIdentificacion,
            'identificacion': self._identificacion,
            'correo': self._cuenta._correo,
            'contrasenia': self._cuenta._clave,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'telefono': self._telefono,
            'ciclo': self._ciclo,
            'paralelo': self._paralelo
        }

    def deserializar(self, data):
        persona = Persona()
        persona._id = data['id']
        persona._tipoIdentificacion = data['tipoIdentificacion']
        persona._identificacion = data['identificacion']
        persona._cuenta._correo = data['correo']
        persona._cuenta._clave = data['contrasenia']
        persona._nombre = data['nombre']
        persona._apellido = data['apellido']
        persona._telefono = data['telefono']
        persona._ciclo = data['ciclo']
        persona._paralelo = data['paralelo']
        return persona