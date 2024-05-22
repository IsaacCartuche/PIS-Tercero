from modelo.rol import EnumRolUsuario
class Cuenta:
    def __init__(self):
        self.__id = 0
        self.__correo = ''
        self.__clave = ''
        self.__rol = EnumRolUsuario

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        self.__correo = value

    @property
    def _clave(self):
        return self.__clave

    @_clave.setter
    def _clave(self, value):
        self.__clave = value

    @property
    def _rol(self):
        return self.__rol

    @_rol.setter
    def _rol(self, value):
        self.__rol = value

