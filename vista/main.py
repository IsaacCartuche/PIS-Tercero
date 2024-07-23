import json
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo JSON
with open('notas.json', 'r') as file:
    data = json.load(file)

# Convertir los datos a un formato más adecuado para pandas
records = []
for student in data:
    for nota in student['notas']:
        records.append({
            'id': student['id'],
            'Ciclo': student['Ciclo'],
            'Paralelo': student['Paralelo'],
            'Unidad': nota['unidad'],
            'Nota': nota['nota']
        })

# Crear un DataFrame
df = pd.DataFrame(records)

# Obtener la lista de ciclos únicos
ciclos = df['Ciclo'].unique()

# Crear un gráfico de dispersión para cada ciclo
for ciclo in ciclos:
    # Aumentar el tamaño y la resolución de la figura
    plt.figure(figsize=(20, 12), dpi=300)
    
    # Filtrar datos para el ciclo actual
    ciclo_data = df[df['Ciclo'] == ciclo]
    
    # Crear el gráfico de dispersión con más detalles
    for unidad in [1, 2, 3]:
        unidad_data = ciclo_data[ciclo_data['Unidad'] == unidad]
        plt.scatter(unidad_data['id'], unidad_data['Nota'], 
                    label=f'Unidad {unidad}', 
                    s=50,  # Aumentar el tamaño de los puntos
                    alpha=0.6)  # Añadir transparencia
    
    # Añadir más detalles y estilos a la gráfica
    plt.title(f'Notas por Unidad - Ciclo {ciclo}', fontsize=20, fontweight='bold')
    plt.xlabel('ID del Estudiante', fontsize=16)
    plt.ylabel('Nota', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Añadir un texto explicativo
    plt.text(0.05, 0.95, f'Total de estudiantes: {len(ciclo_data["id"].unique())}', 
             transform=plt.gca().transAxes, fontsize=12, 
             verticalalignment='top')
    
    # Ajustar los límites de los ejes
    plt.xlim(ciclo_data['id'].min() - 1, ciclo_data['id'].max() + 1)
    plt.ylim(0, 10)
    
    # Añadir un color de fondo suave
    plt.gca().set_facecolor('#f0f0f0')
    
    # Guardar el gráfico como imagen vectorial (más lento de procesar)
    plt.savefig(f'grafico_ciclo_{ciclo}.svg', format='svg', bbox_inches='tight')
    plt.close()

print("Se han generado los gráficos de dispersión para cada ciclo.")






















# import json
# import pandas as pd
# import matplotlib.pyplot as plt

# # Leer el archivo JSON
# with open('notas.json', 'r') as file:
#     data = json.load(file)

# # Convertir los datos a un formato más adecuado para pandas
# records = []
# for student in data:
#     for nota in student['notas']:
#         records.append({
#             'id': student['id'],
#             'Ciclo': student['Ciclo'],
#             'Paralelo': student['Paralelo'],
#             'Unidad': nota['unidad'],
#             'Nota': nota['nota']
#         })

# # Crear un DataFrame
# df = pd.DataFrame(records)

# # Obtener la lista de ciclos únicos
# ciclos = df['Ciclo'].unique()

# # Crear un gráfico de dispersión para cada ciclo
# for ciclo in ciclos:
#     plt.figure(figsize=(10, 6))
    
#     # Filtrar datos para el ciclo actual
#     ciclo_data = df[df['Ciclo'] == ciclo]
    
#     # Crear el gráfico de dispersión
#     for unidad in [1, 2, 3]:
#         unidad_data = ciclo_data[ciclo_data['Unidad'] == unidad]
#         plt.scatter(unidad_data['id'], unidad_data['Nota'], label=f'Unidad {unidad}')
    
#     plt.title(f'Notas por Unidad - Ciclo {ciclo}')
#     plt.xlabel('ID del Estudiante')
#     plt.ylabel('Nota')
#     plt.legend()
#     plt.grid(True)
    
#     # Guardar el gráfico como imagen
#     plt.savefig(f'grafico_ciclo_{ciclo}.png')
#     plt.close()

# print("Se han generado los gráficos de dispersión para cada ciclo.")