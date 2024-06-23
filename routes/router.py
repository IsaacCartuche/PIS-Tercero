from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, url_for
from controlador.estudianteDaoControl import EstudianteControl
from controlador.docenteDaoControl import DocenteDaoControl, Docente
#import json

router = Blueprint('api', __name__)

@router.route('/')
def home():
    return render_template('index.html')


@router.route('/login')
def login():
    return render_template('login.html')

@router.route('/informativa')
def informativa():
    return render_template('404.html')

@router.route('/sugerencias')
def sugerencias():
    return render_template('contact.html')

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
    password_="12345678"
    lista_cursos=[]
    d= Docente()
    for docente in lista_docente:
        if docente._correo == email  and password==password_:
            d._nombre = docente._nombre
            d._apellido= docente._apellido
            for doc in lista_docente:
                if doc._correo==email:
                    lista_cursos.append([doc._materia,doc._ciclo])
            return render_template('docente.html',lista_cursos=lista_cursos,docente=d)

    return redirect(url_for('login'))

@router.route('/verAlumnos_ciclo')
def verAlumnos_ciclo():
    ciclo= request.args.get('ciclo')
    dao_estudiante = EstudianteControl()
    lista_estudiante = dao_estudiante._lista
    lista_estudiante = lista_estudiante.toArray 
    lista_filtrada=[]
    for estudiante in lista_estudiante:
        print(estudiante._ciclo)
        if estudiante._ciclo == int(ciclo):
            lista_filtrada.append(estudiante)
    
    return render_template('listaEstudiantes.html',lista_estudiantes=lista_filtrada)
