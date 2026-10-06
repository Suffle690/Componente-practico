from models import Estudiante
from shared.json_manager import GestorJSON


gestor = GestorJSON("data/estudiantes.json")


def obtener_estudiantes():
    datos = gestor.leer()

    estudiantes = []

    for dato in datos:
        estudiante = Estudiante.desde_diccionario(dato)
        estudiantes.append(estudiante)

    return estudiantes


def guardar_estudiantes(estudiantes):
    datos = []

    for estudiante in estudiantes:
        datos.append(estudiante.a_diccionario())

    gestor.guardar(datos)


def crear_estudiante(nombre, apellido, email, carnet):

    estudiantes = obtener_estudiantes()

    for estudiante in estudiantes:

        if estudiante.email.lower() == email.lower():
            return False, "El email ya existe."

        if estudiante.carnet.lower() == carnet.lower():
            return False, "El carnet ya existe."

    id = 1

    if len(estudiantes) > 0:
        id = estudiantes[-1].id + 1

    estudiante = Estudiante(
        id,
        nombre,
        apellido,
        email,
        carnet
    )

    estudiantes.append(estudiante)

    guardar_estudiantes(estudiantes)

    return True, "Estudiante creado correctamente."


def listar_estudiantes():

    estudiantes = obtener_estudiantes()

    return estudiantes


def buscar_estudiante(texto):

    estudiantes = obtener_estudiantes()

    encontrados = []

    for estudiante in estudiantes:

        if texto.lower() in estudiante.nombre.lower():
            encontrados.append(estudiante)

        elif texto.lower() in estudiante.apellido.lower():
            encontrados.append(estudiante)

        elif texto.lower() in estudiante.email.lower():
            encontrados.append(estudiante)

        elif texto.lower() in estudiante.carnet.lower():
            encontrados.append(estudiante)

    return encontrados


def eliminar_estudiante(id):

    estudiantes = obtener_estudiantes()

    nuevos = []

    encontrado = False

    for estudiante in estudiantes:

        if estudiante.id == id:
            encontrado = True
        else:
            nuevos.append(estudiante)

    if encontrado:
        guardar_estudiantes(nuevos)
        return True

    return False


def actualizar_estudiante(id, nombre, apellido, email, carnet):

    estudiantes = obtener_estudiantes()

    for estudiante in estudiantes:

        if estudiante.id == id:

            estudiante.nombre = nombre
            estudiante.apellido = apellido
            estudiante.email = email
            estudiante.carnet = carnet

            guardar_estudiantes(estudiantes)

            return True

    return False


def agregar_nota(id, materia, nota):

    estudiantes = obtener_estudiantes()

    for estudiante in estudiantes:

        if estudiante.id == id:

            estudiante.agregar_nota(materia, nota)

            guardar_estudiantes(estudiantes)

            return True

    return False


def materias_ofertadas():

    estudiantes = obtener_estudiantes()

    materias = set()

    for estudiante in estudiantes:

        for materia in estudiante.materias:
            materias.add(materia["materia"])

    return materias


def estudiantes_en_comun(id1, id2):

    estudiantes = obtener_estudiantes()

    estudiante1 = None
    estudiante2 = None

    for estudiante in estudiantes:

        if estudiante.id == id1:
            estudiante1 = estudiante

        if estudiante.id == id2:
            estudiante2 = estudiante

    if estudiante1 is None or estudiante2 is None:
        return set()

    return estudiante1.materias_en_comun(estudiante2)