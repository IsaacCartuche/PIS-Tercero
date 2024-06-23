import sys
sys.path.append('../')
<<<<<<< HEAD


from controlador.estudianteDaoControl import EstudianteControl
from controlador.docenteDaoControl import DocenteDaoControl
from modelo.enumIdentificacion import EnumIdentificacion
try:
    """ estudi = EstudianteControl()
    doc = DocenteDaoControl()
    
    estudi._estudiante._tipoIdentificacion = 'CEDULA'
    estudi._estudiante._identificacion = '1105526436'
    estudi._estudiante._nombre = 'Juan'
    estudi._estudiante._apellido = 'Perez'
    estudi._estudiante._telefono = '0987654321'
    estudi._estudiante._matricula = 1
    estudi._estudiante._fechaNacimiento = '2000-01-01'
    estudi.save
    
    estudi._estudiante._tipoIdentificacion = 'CEDULA'
    estudi._estudiante._identificacion = '1105526437'
    estudi._estudiante._nombre = 'Anthony'
    estudi._estudiante._apellido = 'Gutierrez'
    estudi._estudiante._telefono = '0987654321'
    estudi._estudiante._matricula = 2
    estudi._estudiante._fechaNacimiento = '2000-01-01'
    estudi.save
    
    doc._docente._tipoIdentificacion = 'CEDULA'
    doc._docente._identificacion = '1105526438'
    doc._docente._nombre = 'Juan'
    doc._docente._apellido = 'Perez'
    doc._docente._telefono = '0987654321'
    doc._docente._especialidad = 'Matematicas'
    doc._docente._aniosExperienciaDocente = 10
    doc._docente._cubiculo = 'A1'
    doc.save
    
    doc._docente._tipoIdentificacion = 'CEDULA'
    doc._docente._identificacion = '1105526439'
    doc._docente._nombre = 'Anthony'
    doc._docente._apellido = 'Gutierrez'
    doc._docente._telefono = '0987654321'
    doc._docente._especialidad = 'Matematicas'
    doc._docente._aniosExperienciaDocente = 10
    doc._docente._cubiculo = 'A1'
    doc.save """


except Exception as e:
    print(e)
=======
 
from controlador.cursaDaoControl import CursaDaoControl
from controlador.periodoDaoControl import PeriodoDaoControl

#pc. = PeriodoDaoControl()
#ec = EstudianteDaoControl()
#cc = CursaDaoControl()
 
>>>>>>> origin/Anthony
