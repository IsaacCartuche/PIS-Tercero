import enum
class EnumRolUsuario(enum.Enum):
    USUARIO = 'USUARIO'
    ADMIN = 'ADMIN'

    def __str__(self):
        return self.value