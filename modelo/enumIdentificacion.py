import enum

class EnumIdentificacion(enum.Enum):
    CEDULA = 'CEDULA'
    PASAPORTE = 'PASAPORTE'
    OTRO = 'OTRO'


    def __str__(self) -> str:
        return self.name