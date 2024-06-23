import pandas as pd
from scipy.stats import chi2_contingency

from modelo.estadistica import Estadistica

class EstadisticaControl:
    def __init__(self):

        self.calificaciones = []

    def agregar_calificacion(self, materia, unidad, calificacion):
        self.calificaciones.append({
            'materia': materia,
            'unidad': unidad,
            'calificacion': calificacion
        })

    def generar_tabla_contingencia(self):
        df = pd.DataFrame(self.calificaciones)
        tabla_contingencia = pd.crosstab(df['materia'], df['unidad'], values=df['calificacion'], aggfunc='mean')
        return tabla_contingencia

    def calcular_p_valor(self):
        tabla_contingencia = self.generar_tabla_contingencia()
        chi2, p_valor, _, _ = chi2_contingency(tabla_contingencia.fillna(0))
        return p_valor

    
    