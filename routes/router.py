from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, url_for
from controlador.estudianteDaoControl import EstudianteControl
from controlador.docenteDaoControl import DocenteDaoControl, Docente
import json
#import json
import os, openpyxl
router = Blueprint('api', __name__)
lista_cursos=[]
d= Docente()

@router.route('/')
def home():
    return render_template('index.html')


@router.route('/login')
def login():
    return render_template('login.html')


@router.route('/cerrarSesion')
def cerrarSesion():
    return redirect(url_for('api.home'))


@router.route('/usuario_login', methods=['POST'])
def usuario_login():
    dao_docente=DocenteDaoControl()
    lista_docente= dao_docente._lista
    lista_docente=lista_docente.toArray
    email= request.form.get('email')
    password=request.form.get('password')
    

    for docente in lista_docente:
        if docente._cuenta._correo == email  and password==docente._cuenta._clave:
            d._nombre = docente._nombre
            d._apellido= docente._apellido
            for doc in lista_docente:
                if doc._correo==email:
                    lista_cursos.append([doc._materia,doc._ciclo])
            return render_template('docente.html',lista_cursos=lista_cursos,docente=d)
        else:
            print("es admin")
            pass

    return redirect(url_for('api.login'))

@router.route('/verAlumnos_ciclo')
def verAlumnos_ciclo():
    ciclo= request.args.get('ciclo')
    dao_estudiante = EstudianteControl()
    lista_estudiante = dao_estudiante._lista
    lista_estudiante = lista_estudiante.toArray 
    lista_filtrada=[]
    for estudiante in lista_estudiante:
        #print(estudiante._ciclo)
        if estudiante._ciclo == int(ciclo):
            lista_filtrada.append(estudiante)
    
    
    with open('data/notas.json', 'r') as file:
        data = json.load(file)
        
    
    print(data)
    return render_template('listaEstudiantes.html',lista_estudiantes=lista_filtrada, data = data)


@router.route('/subir_notas')
def subir_notas():
    
    return render_template('agregarArchivos.html')

@router.route('/upload', methods=['POST'])
def upload():
    file = request.files["uploadFile"]
    #print(file)
    file.save(file.filename)
    excel_dataframe = openpyxl.load_workbook(str(file.filename))
    dataframe = excel_dataframe.active
    data = []
    for row in range(1, dataframe.max_row):
        _row = [row,]
        for col in dataframe.iter_cols(1, dataframe.max_column):
            print(col[row].value)
            _row.append(col[row].value)
        data.append(_row)
    return render_template('docente.html',lista_cursos=lista_cursos,docente=d)




##############################################################################################################################################################
##############################################################################################################################################################


# from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, url_for
# from controlador.conexion.conexion import Conexion 

# import os, openpyxl

# router = Blueprint('api', __name__)
# db = Conexion('ISAAC', 'Isaac2004Cartuche', '192.168.1.10/xe')
# db.connect()

# @router.route('/')
# def home():
#     return render_template('index.html')

# @router.route('/login')
# def login():
#     return render_template('login.html')

# @router.route('/cerrarSesion')
# def cerrarSesion():
#     return redirect(url_for('api.home'))

# @router.route('/usuario_login', methods=['POST'])
# def usuario_login():
#     email = request.form.get('email')
#     password = request.form.get('password')
    
#     query = """
#     SELECT d.nombre, d.apellido, d.correo, d.materia, d.ciclo, c.rol
#     FROM docentes d
#     JOIN cuentas c ON d.id_cuenta = c.id
#     WHERE c.correo = :1 AND c.clave = :2
#     """
#     docente = db.execute_query(query, (email, password))
    
#     if docente and docente[0]['rol'] == 'USUARIO':
#         d = docente[0]
#         lista_cursos = [[d['materia'], d['ciclo']]]
#         return render_template('docente.html', lista_cursos=lista_cursos, docente=d)
#     else:
#         return redirect(url_for('api.login'))

# @router.route('/verAlumnos_ciclo')
# def verAlumnos_ciclo():
#     ciclo = request.args.get('ciclo')
    
#     query_estudiantes = """
#     SELECT * FROM estudiantes WHERE ciclo = :1
#     """
#     lista_filtrada = db.execute_query(query_estudiantes, (ciclo,))
    
#     query_notas = """
#     SELECT e.id, n.unidad, n.nota
#     FROM estudiantes e
#     JOIN notas n ON e.id = n.id_estudiante
#     WHERE e.ciclo = :1
#     """
#     notas = db.execute_query(query_notas, (ciclo,))
    
#     # Organizar las notas por estudiante
#     data = {}
#     for nota in notas:
#         if nota['id'] not in data:
#             data[nota['id']] = {'notas': []}
#         data[nota['id']]['notas'].append({
#             'unidad': nota['unidad'],
#             'nota': nota['nota']
#         })
    
#     return render_template('listaEstudiantes.html', lista_estudiantes=lista_filtrada, data=data)

# @router.route('/subir_notas')
# def subir_notas():
#     return render_template('agregarArchivos.html')

# @router.route('/upload', methods=['POST'])
# def upload():
#     file = request.files["uploadFile"]
#     file.save(file.filename)
#     excel_dataframe = openpyxl.load_workbook(str(file.filename))
#     dataframe = excel_dataframe.active
    
#     for row in range(2, dataframe.max_row + 1):  # Asumiendo que la primera fila es encabezado
#         id_estudiante = dataframe.cell(row, 1).value
#         unidad = dataframe.cell(row, 2).value
#         nota = dataframe.cell(row, 3).value
        
#         query = """
#         INSERT INTO notas (id_estudiante, unidad, nota)
#         VALUES (:1, :2, :3)
#         """
#         db.execute_dml(query, (id_estudiante, unidad, nota))
    
#     os.remove(file.filename)  # Eliminar el archivo después de procesarlo
    
#     return redirect(url_for('api.verAlumnos_ciclo', ciclo=1))  # Ajusta según sea necesario



